def fatorial(num):
    if num <= 0:
       return "Não existe fatorial de zero ou número negativo."
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

num = int(input('Insira um número: '))
resposta = fatorial(num)

print(f'O fatorial de {num} é {resposta}')
