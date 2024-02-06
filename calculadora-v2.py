
#Funções
def sum( a, b):
    return a + b
def sub( a, b):
    return a - b
def mult( a, b):
    return a * b
def div( a, b):
    if b != 0:
        return a / b
    else:
        return 'Impossível dividir por zero'

value1 = float(input('Informe o valor 1: '))
operador = input('Informe o operador:  ')
value2 = float(input('Informe o valor 2: '))

if operador == '+':
    print('O resultado da conta é', sum(value1,value2))

elif operador == '-':
    print('O resultado da conta é', sub(value1,value2))

elif operador == '*':
    print('O resultado da conta é', mult(value1,value2))

elif operador == '/':
    print('O resultado da conta é', div(value1,value2))

else:
    print('Operador inválido')

