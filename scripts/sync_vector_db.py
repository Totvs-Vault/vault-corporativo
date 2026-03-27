import os
import glob
from google import genai
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

def sync_to_vector_db():
    md_files = glob.glob(f"{CONTENT_DIR}/*.md")
    
    for file_path in md_files:
        filename = os.path.basename(file_path)
        
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
            
        chunks = chunk_text(text)
        vectors = []
        
        for i, chunk in enumerate(chunks):
            if not chunk.strip(): continue
            
            # 2. Usa o motor oficial atual com a sintaxe nova
            response = client.models.embed_content(
                model='text-embedding-004',
                contents=chunk,
            )
            
            # Extrai os 768 números
            embedding_values = response.embeddings[0].values
            
            chunk_id = f"{filename}-chunk-{i}"
            vectors.append({
                "id": chunk_id, 
                "values": embedding_values, 
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