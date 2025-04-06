# Tabela fixa de palavras reservadas com atributos (exemplo Python)
palavras_reservadas = {
    "if": "controle de fluxo",
    "else": "controle de fluxo",
    "elif": "controle de fluxo",
    "for": "laço",
    "while": "laço",
    "def": "definição de função",
    "return": "retorno de função",
    "True": "valor booleano",
    "False": "valor booleano",
    "import": "importação de módulo",
    "class": "definição de classe",
    "try": "tratamento de exceção",
    "except": "tratamento de exceção",
    "finally": "tratamento de exceção",
    "with": "gerenciamento de contexto",
    "pass": "placeholder",
    "break": "controle de laço",
    "continue": "controle de laço",
    "lambda": "função anônima",
    "global": "escopo de variável",
    "nonlocal": "escopo de variável"
}

# Procedimento de pesquisa
def pesquisar_palavra(palavra):
    if palavra in palavras_reservadas:
        print(f"A palavra '{palavra}' é reservada. Categoria: {palavras_reservadas[palavra]}")
    else:
        print(f"A palavra '{palavra}' NÃO é reservada.")

# Loop interativo para testar
def menu():
    while True:
        print("\n--- Pesquisa em Tabela de Palavras Reservadas ---")
        entrada = input("Digite uma palavra para pesquisar (ou 'sair' para encerrar): ")
        if entrada.lower() == "sair":
            print("Encerrando...")
            break
        pesquisar_palavra(entrada)

# Iniciar o programa
if __name__ == "__main__":
    menu()
