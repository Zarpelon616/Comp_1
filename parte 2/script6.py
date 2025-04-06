# Dicionário principal da tabela
tabela_simbolos = {}

# Incluir símbolo
def incluir_simbolo(nome, atributos):
    if nome in tabela_simbolos:
        print("Símbolo já existe.")
    else:
        tabela_simbolos[nome] = atributos
        print(f"Símbolo '{nome}' incluído com sucesso!")

# Atualizar ou adicionar atributos
def atualizar_atributos(nome, novos_atributos):
    if nome in tabela_simbolos:
        tabela_simbolos[nome].update(novos_atributos)
        print(f"Atributos de '{nome}' atualizados.")
    else:
        print("Símbolo não encontrado.")

# Pesquisar símbolo
def pesquisar_simbolo(nome):
    simbolo = tabela_simbolos.get(nome)
    if simbolo:
        print(f"Símbolo encontrado: {nome} -> {simbolo}")
    else:
        print("Símbolo não encontrado.")

# Ordenar e exibir a tabela
def exibir_tabela_ordenada():
    print("\nTabela de Símbolos (Ordenada):")
    for nome in sorted(tabela_simbolos.keys()):
        print(f"{nome} -> {tabela_simbolos[nome]}")

# Remover símbolo
def remover_simbolo(nome):
    if nome in tabela_simbolos:
        del tabela_simbolos[nome]
        print(f"Símbolo '{nome}' removido.")
    else:
        print("Símbolo não encontrado.")

# Menu de interação
def menu():
    while True:
        print("\n--- Tabela de Símbolos ---")
        print("1. Incluir símbolo")
        print("2. Atualizar atributos de símbolo")
        print("3. Pesquisar símbolo")
        print("4. Exibir tabela ordenada")
        print("5. Remover símbolo")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do símbolo: ")
            atributos = {}
            while True:
                chave = input("Nome do atributo (ou 'fim' para parar): ")
                if chave.lower() == 'fim':
                    break
                valor = input(f"Valor de '{chave}': ")
                atributos[chave] = valor
            incluir_simbolo(nome, atributos)

        elif opcao == '2':
            nome = input("Nome do símbolo: ")
            novos = {}
            while True:
                chave = input("Atributo para atualizar (ou 'fim' para parar): ")
                if chave.lower() == 'fim':
                    break
                valor = input(f"Novo valor de '{chave}': ")
                novos[chave] = valor
            atualizar_atributos(nome, novos)

        elif opcao == '3':
            nome = input("Nome do símbolo: ")
            pesquisar_simbolo(nome)

        elif opcao == '4':
            exibir_tabela_ordenada()

        elif opcao == '5':
            nome = input("Nome do símbolo a remover: ")
            remover_simbolo(nome)

        elif opcao == '6':
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o menu
if __name__ == "__main__":
    menu()
