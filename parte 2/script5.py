def ler_numero_em_base():
    print("Bases suportadas: binário (2), octal (8), decimal (10), hexadecimal (16)")
    base_entrada = int(input("Informe a base do número de entrada (2, 8, 10 ou 16): "))
    numero_str = input("Digite o número na base escolhida: ")

    try:
        # Converte a string para decimal
        numero_decimal = int(numero_str, base=base_entrada)
        print(f"Valor armazenado em decimal: {numero_decimal}")
        return numero_decimal
    except ValueError:
        print("Número inválido para a base informada.")
        return None

def formatar_saida(numero_decimal):
    base_saida = int(input("Escolha a base para saída (2 - binário, 8 - octal, 10 - decimal, 16 - hexadecimal): "))
    digitos = int(input("Número mínimo de dígitos (completar com 0 à esquerda se necessário): "))
    sinal_posicao = input("Posição do sinal (+/-): antes ou depois? (Digite 'antes' ou 'depois'): ").strip().lower()

    if base_saida == 2:
        numero_convertido = bin(abs(numero_decimal))[2:]
    elif base_saida == 8:
        numero_convertido = oct(abs(numero_decimal))[2:]
    elif base_saida == 10:
        numero_convertido = str(abs(numero_decimal))
    elif base_saida == 16:
        numero_convertido = hex(abs(numero_decimal))[2:]
    else:
        print("Base de saída inválida.")
        return

    numero_formatado = numero_convertido.zfill(digitos)
    sinal = "-" if numero_decimal < 0 else "+"

    if sinal_posicao == 'antes':
        saida = sinal + numero_formatado
    elif sinal_posicao == 'depois':
        saida = numero_formatado + sinal
    else:
        print("Posição de sinal inválida. Usando padrão (antes).")
        saida = sinal + numero_formatado

    print(f"Saída formatada: {saida}")

def main():
    numero_decimal = ler_numero_em_base()
    if numero_decimal is not None:
        formatar_saida(numero_decimal)

if __name__ == "__main__":
    main()

# exemplo de uso
# Bases suportadas: binário (2), octal (8), decimal (10), hexadecimal (16)
# Informe a base do número de entrada (2, 8, 10 ou 16): "digite 2"
# Digite o número na base escolhida: "digite 1011(11 em binario)"
# Escolha a base para saída (2 - binário, 8 - octal, 10 - decimal, 16 - hexadecimal): "digite 16"
# Número mínimo de dígitos (completar com 0 à esquerda se necessário): "Digite 4"
# Posição do sinal (+/-): antes ou depois? (Digite 'antes' ou 'depois'): "Digite 'antes'"
# resultado esperado deve ser: Saída formatada: +000b
