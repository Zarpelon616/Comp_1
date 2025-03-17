import pdfplumber
import re

def extrair_texto(arquivo):
    """Extrai texto de um PDF e remove caracteres indesejados mantendo legibilidade."""
    try:
        with pdfplumber.open(arquivo) as pdf:
            texto_limpo = []
            for pagina in pdf.pages:
                texto = pagina.extract_text()
                if texto:
                    # Substitui múltiplos espaços por um único espaço
                    texto = re.sub(r'\s+', ' ', texto)
                    texto_limpo.append(texto.strip())  # Remove espaços extras no início e fim
            return "\n\n".join(texto_limpo)  # Junta com duas quebras de linha entre parágrafos
    except Exception as e:
        print(f"Erro ao processar o PDF: {e}")
        return ""

arquivo = "teste.pdf"

# Extrai o texto filtrado do PDF
texto_extraido = extrair_texto(arquivo)

# Exibir o texto limpo
print(texto_extraido)
