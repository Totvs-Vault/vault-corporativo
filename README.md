# 🧠 Vault Corporativo - Totvs

Bem-vindo ao repositório oficial do **Vault Corporativo**, a base de conhecimento inteligente e automatizada da nossa equipe. 

Este projeto não é apenas um site de documentação; é um "Cérebro Corporativo" alimentado por Inteligência Artificial que lê, processa, indexa e publica nossos manuais, processos e playbooks de forma 100% automatizada.

🌐 **Acesse o site oficial aqui:** [https://totvs-vault.github.io/vault-corporativo/](https://totvs-vault.github.io/vault-corporativo/)

---

## 👔 Guia Rápido para Editores (Como publicar documentos)

Você não precisa instalar nenhum programa, usar terminais ou saber programar para alimentar o Vault. O processo é totalmente visual direto pelo navegador:

1. Navegue até a pasta `input_docs` aqui neste repositório.
2. No canto superior direito, clique em **Add file** > **Upload files**.
3. Arraste o seu arquivo do seu computador para dentro da área tracejada na tela.
4. Clique no botão verde **Commit changes**.
5. **Pronto!** Vá tomar um café. ☕ 

Em cerca de 2 a 3 minutos, nossos robôs vão ler o seu documento, extrair os textos e imagens, enviar para a memória da Inteligência Artificial e publicar no site oficial.

### ⚠️ Regras de Formato
O nosso motor de IA foi treinado para extrair texto, tabelas e imagens com perfeição dos seguintes formatos:

* 📄 **.PDF** (Manuais e Documentos)
* 📝 **.DOCX** (Microsoft Word)
* 📊 **.PPTX** (Microsoft PowerPoint)

> **Usa Google Workspace ou LibreOffice?**
> O sistema não aceita links do Google Docs ou arquivos `.odt`/`.odp`. 
> * Se usar o Google, vá em `Arquivo > Fazer download` e escolha Word (`.docx`) ou PDF.
> * Se usar o LibreOffice, vá em `Salvar Como...` e escolha `Word 2007-365 (.docx)`.

*(Dica: Para atualizar um documento que já existe no site, basta fazer o upload do arquivo novo com **exatamente o mesmo nome** do arquivo antigo).*

---

## ⚙️ Sob o Capô (Para a equipe de TI / Arquitetura)

Este projeto utiliza uma esteira CI/CD via GitHub Actions com conversão baseada em Python e publicação estática via Quartz.

### A Esteira de Automação (Workflows)
1. **Vault Auto-Convert & Sync:** Disparado assim que um arquivo é inserido em `input_docs`.
   * Utiliza `pymupdf4llm` para extração inteligente de layout e imagens de PDFs.
   * Utiliza `mammoth` para extração de `.docx` preservando formatação e extraindo mídias para a pasta `assets`.
   * Utiliza `python-pptx` para varredura de slides, textos e blobs de imagens.
   * Envia os dados vetorizados para o banco de dados **Pinecone** integrado com LLM.
2. **Deploy Quartz Site:** Disparado automaticamente após o término da conversão. Compila os arquivos Markdown gerados e faz o deploy no GitHub Pages.

### Estrutura de Pastas
* `/input_docs`: Gaveta de entrada (Dropzone) para os usuários finais.
* `/site`: Motor do Quartz e front-end da base de conhecimento.
* `/site/content`: Onde os arquivos `.md` convertidos residem.
* `/site/content/assets`: Onde as imagens extraídas dos documentos são armazenadas.
* `/scripts`: Scripts em Python responsáveis pela engenharia de conversão e extração.
* `/.github/workflows`: Arquitetura dos robôs de automação.