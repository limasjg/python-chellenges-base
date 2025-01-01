while True:
    emprestimo = float(input("Informe o valor do empréstimo: "))
    if emprestimo <= 0:
        print("O valor do empréstimo não pode ser menor ou igual a zero.")
    else:
        break

while True:
    taxa_juros = float(input("Informe a taxa de juros mensal (em %): "))
    if taxa_juros <= 0:
        print("A taxa de juros deve ser maior que zero.")
    else:
        taxa_juros /= 100  # Converte a taxa para decimal
        break

while True:
    numero_parcelas = int(input("Informe o número de parcelas: "))
    if numero_parcelas < 1:
        print("O número de parcelas deve ser maior ou igual a 1.")
    else:
        break

# Fórmula: P = (V * i) / (1 - (1 + i) ** -n)
parcela = (emprestimo * taxa_juros) / (1 - (1 + taxa_juros) ** -numero_parcelas)
total_pago = parcela * numero_parcelas
print(f"O valor da parcela será de R$ {parcela:.2f} e o total pago no final será {parcela * numero_parcelas:.2f}")
print(f"Você terá pago {total_pago - emprestimo:.2f}" )

