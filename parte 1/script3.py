import pdfplumber
import re

def extrair_texto(arquivo):
    """Extrai texto de um PDF e adiciona numeração às linhas."""
    try:
        with pdfplumber.open(arquivo) as pdf:
            linhas_numeradas = []
            linha_numero = 1  # Contador de linhas
            
            for pagina in pdf.pages:
                texto = pagina.extract_text()
                if texto:
                    # Remove múltiplos espaços e mantém a formatação básica
                    texto = re.sub(r'\s+', ' ', texto).strip()
                    linhas = texto.split('. ')  # Separa frases para numerar melhor
                    
                    for linha in linhas:
                        if linha.strip():  # Evita linhas vazias
                            linhas_numeradas.append(f"{linha_numero}. {linha.strip()}")
                            linha_numero += 1
            
            return "\n".join(linhas_numeradas)  # Junta tudo com quebras de linha
    except Exception as e:
        print(f"Erro ao processar o PDF: {e}")
        return ""

arquivo = "teste.pdf"

# Extrai o texto numerado
texto_numerado = extrair_texto(arquivo)

# Exibir o texto numerado
print(texto_numerado)
