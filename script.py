import pdfplumber

def extrair_caracteres(arquivo):
    caracteres = []
    try:
        with pdfplumber.open(arquivo) as pdf:
            for pagina in pdf.pages:
                texto = pagina.extract_text()
                if texto:
                    caracteres.extend(list(texto))  # Transforma o texto em lista de caracteres
        return caracteres
    except Exception as e:
        print(f"Erro ao processar o PDF: {e}")
        return []

#exemplo usado
arquivo = "teste.pdf" #Caminho arquivo
caracteres_extraidos = extrair_caracteres(arquivo)

# Exibir os caracteres extraídos
print(caracteres_extraidos)
print("".join(caracteres_extraidos))
