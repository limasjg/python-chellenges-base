import random

numero_aleatorio = random.randint(1, 10)

chances = 5

numero = int(input('Digite um número: '))

while numero != numero_aleatorio:
    chances -= 1
    if chances == 0:
        print('Você perdeu o número era', numero_aleatorio)
        break
    else:
        numero = int(input('você errou, digite outro número: '))

else:
    print('você acertou', numero_aleatorio)

    