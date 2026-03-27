import os
import glob
import unicodedata
from google import genai
from google.genai import types
from pinecone import Pinecone

# 1. Conecta usando a NOVA biblioteca do Google
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
pc = Pinecone(api_key=os.environ["VECTOR_DB_API_KEY"])
index = pc.Index("vault-index") 

CONTENT_DIR = "site/content" 

def chunk_text(text, max_chars=1000):
    """Quebra o texto em pedaços para a IA conseguir ler e pesquisar melhor"""
    paragraphs = text.split('\n\n')
    chunks = []
    current_chunk = ""
    for p in paragraphs:
        if len(current_chunk) + len(p) < max_chars:
            current_chunk += p + "\n\n"
        else:
            if current_chunk.strip():
                chunks.append(current_chunk.strip())
            current_chunk = p + "\n\n"
    if current_chunk.strip():
        chunks.append(current_chunk.strip())
    return chunks

def sanitize_id(text):
    """Remove acentos e caracteres especiais para o Pinecone aceitar o ID"""
    texto_sem_acento = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
    # Substitui espaços por hifens só por segurança extra
    return texto_sem_acento.replace(' ', '-')

def sync_to_vector_db():
    md_files = glob.glob(f"{CONTENT_DIR}/*.md")
    
    for file_path in md_files:
        filename = os.path.basename(file_path)
        
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
            
        chunks = chunk_text(text)
        vectors = []
        
        # Cria um nome seguro (sem acento) para usar como ID
        safe_filename = sanitize_id(filename)
        
        for i, chunk in enumerate(chunks):
            if not chunk.strip(): continue
            
            # O Novo Motor Oficial
            response = client.models.embed_content(
                model='gemini-embedding-001',
                contents=chunk,
                config=types.EmbedContentConfig(
                    task_type="RETRIEVAL_DOCUMENT",
                    output_dimensionality=3072 
                )
            )
            
            # Extrai os números
            embedding_values = response.embeddings[0].values
            
            # Usa o nome limpo para o crachá!
            chunk_id = f"{safe_filename}-chunk-{i}"
            
            vectors.append({
                "id": chunk_id, 
                "values": embedding_values, 
                # Mas mantém o nome original (com acento) guardado no metadata
                "metadata": {"source": filename, "text": chunk, "status": "oficial"}
            })
            
        if vectors:
            batch_size = 50
            for i in range(0, len(vectors), batch_size):
                batch = vectors[i:i + batch_size]
                index.upsert(vectors=batch)
                
        print(f"🧠 Sincronizado com IA (em fatias): {filename}")

if __name__ == "__main__":
    sync_to_vector_db()