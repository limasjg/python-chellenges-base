def fatorial(num):

    if num <= 0:
        print('Não existe fatorial de zero ou número negativo ')
    else:
        for i in range(1, num):
            mult =  i * num
            soma.append(mult)


num = int(input('Insira um número: '))
resposta = fatorial(num)
soma = []
total = sum(soma)


print(f'O fatorial de {num} é {total}')
