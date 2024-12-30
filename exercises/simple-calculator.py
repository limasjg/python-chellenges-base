def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return print("Erro! impossível dividir por zero.")

print("----------------Calculadora-----------------")

num1 = float(input("Digite o primeiro valor: "))
operador = input("Digite o Operador (exemplo: +, -, * ou / ): ")
num2 = float(input("Digite o Segundo valor: "))

if operador == '+':   
    print("O resultado é:", soma(num1,num2)) 
elif operador == '-':
    print("O resultado é:", sub(num1,num2)) 
elif operador == '*':
    print("O resultado é:", mult(num1,num2)) 
elif operador == '/':
    print("O resultado é:", div(num1,num2))     
else:
    print("Operador inválido.")
    