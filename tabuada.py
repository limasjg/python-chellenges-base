num = int(input('Digite um número de 1 a 9 para saber sua tabuada: '))
if num < 1 or num > 9:
    print('Erro')
else:
    print(f'A tabuada de {num} é:')
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')