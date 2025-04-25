import os
import hashlib 
import exifread #extrai os metadados da imagem
from docx import Document # provavelmente um biblioteca que extrai texto
import PyPDF2

# Função para gerar hash MD5 e SHA256 de um arquivo
def gerar_hash(arquivo):
    hash_md5 = hashlib.md5()
    hash_sha256 = hashlib.sha256()
    with open(arquivo, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
            hash_sha256.update(chunk)
    return hash_md5.hexdigest(), hash_sha256.hexdigest()

# Função para extrair metadados de imagens (JPEG/PNG)
def metadados_imagem(arquivo):
    with open(arquivo, 'rb') as f:
        tags = exifread.process_file(f)
        return tags

# Função para extrair metadados de documentos .docx
def metadados_docx(arquivo):
    doc = Document(arquivo)
    props = doc.core_properties
    return {
        "Autor": props.author,
        "Título": props.title,
        "Criado em": props.created,
        "Modificado em": props.modified
    }

# Função para extrair metadados de PDF
def metadados_pdf(arquivo):
    with open(arquivo, 'rb') as f:
        pdf = PyPDF2.PdfReader(f)
        info = pdf.metadata
        return info

# Função principal
def extrair_metadados(caminho_arquivo):
    if not os.path.isfile(caminho_arquivo): # verifica se o arquivo não existe
        print("Arquivo não encontrado.")
        return

    nome_arquivo = os.path.basename(caminho_arquivo) #basename extrai apenas a última parte do caminh
    tamanho = os.path.getsize(caminho_arquivo) # captura o tamanho do arquivo em bytes
    md5, sha256 = gerar_hash(caminho_arquivo)

    print(f"\n📄 Arquivo: {nome_arquivo}")
    print(f"📏 Tamanho: {tamanho} bytes")
    print(f"🔑 MD5: {md5}")
    print(f"🔒 SHA256: {sha256}")

    extensao = nome_arquivo.split('.')[-1].lower()

    try:
        if extensao in ['jpg', 'jpeg', 'png']:
            print("\n🔍 Metadados da imagem:")
            metadados = metadados_imagem(caminho_arquivo)
            for tag, valor in metadados.items():
                print(f"{tag}: {valor}")

        elif extensao == 'docx':
            print("\n🔍 Metadados do documento .docx:")
            metadados = metadados_docx(caminho_arquivo)
            for chave, valor in metadados.items():
                print(f"{chave}: {valor}")

        elif extensao == 'pdf':
            print("\n🔍 Metadados do PDF:")
            metadados = metadados_pdf(caminho_arquivo)
            for chave, valor in metadados.items():
                print(f"{chave}: {valor}")

        else:
            print("\n❗ Formato não suportado para metadados específicos.")

    except Exception as e:
        print(f"Erro ao extrair metadados: {e}")

# Execução
if __name__ == "__main__": # preciso entender esa função
    caminho = r"C:\Users\jcfab\Desktop\Comparar\ola.docx"
    extrair_metadados(caminho) # essa é a primeira função a ser executada
