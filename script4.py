import pdfplumber
import re
from collections import defaultdict

def extrair_palavras(arquivo):
    """Extrai palavras e associa às linhas em que ocorrem."""
    palavras_linhas = defaultdict(set)  # Usamos set para evitar duplicação de linhas por palavra
    try:
        with pdfplumber.open(arquivo) as pdf:
            linha_numero = 1  # Contador de linhas
            
            for pagina in pdf.pages:
                texto = pagina.extract_text()
                if texto:
                    # Remove múltiplos espaços e mantém a formatação básica
                    texto = re.sub(r'\s+', ' ', texto).strip()
                    linhas = texto.split('. ')  # Divide o texto em frases
                    
                    for linha in linhas:
                        if linha.strip():  # Evita linhas vazias
                            palavras = re.findall(r'\b\w+\b', linha.lower())  # Encontra palavras (ignora maiúsculas/minúsculas)
                            for palavra in palavras:
                                palavras_linhas[palavra].add(linha_numero)  # Adiciona o número da linha
                            linha_numero += 1

            # Ordena as palavras alfabeticamente
            palavras_ordenadas = sorted(palavras_linhas.items())
            return palavras_ordenadas
    except Exception as e:
        print(f"Erro ao processar o PDF: {e}")
        return []

arquivo = "teste.pdf"

# Extrai as palavras e suas linhas
referencias_palavras = extrair_palavras(arquivo)

# Exibir a tabela de referências cruzadas
print("Tabela de Referências Cruzadas (Palavra -> Linhas):")
for palavra, linhas in referencias_palavras:
    print(f"{palavra.capitalize()} -> {sorted(linhas)}")
