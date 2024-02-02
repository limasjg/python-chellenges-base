# Função que verifica se número é primo
def eh_primo(num):
    if num <=1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


numero = int(input('Digite um número: '))

primos = []

for i in range(2, numero + 1):
    if eh_primo(i):
        primos.append(i)   

if len(primos) > 0:
    print(f'os númeos primos até {numero} são {primos}')
else:
    print(f'Não existe número primo até {numero}')



    

