# Inicializando as variáveis
inicial = 0
juros = 0
tempo = 0

# Solicita o valor inicial
while inicial <= 0:
    inicial = float(input("Qual o valor inicial que você irá investir? "))
    if inicial <= 0:
        print("O investimento inicial precisa ser maior que zero.")
    else:
        print(f"Valor inicial: {inicial}")

# Solicita a taxa de juros
while juros <= 0:
    juros = float(input("Informe a taxa de juros (em %): "))
    if juros <= 0:
        print("A taxa de juros precisa ser maior que zero.")
    else:
        juros /= 100  # Converte a taxa de juros para decimal
        print(f"Taxa de juros: {juros:.2%}")

# Solicita o prazo em meses
while tempo <= 0:
    tempo = int(input("Qual o prazo em meses? "))
    if tempo <= 0:
        print("O prazo precisa ser maior que zero.")
    else:
        print(f"Prazo: {tempo} meses")

# Calcula o montante
montante = inicial * (1 + juros) ** tempo

# Exibe o resultado final
print(f"Ao final de {tempo} meses, você terá R$ {montante:.2f}")
