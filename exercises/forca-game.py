# Importa de random
import random

#Lista de palalvras
palavras = ['gandalf', 'hermione', 'skywalker', 'dumbledore', 'spock', 'frodo', 'aragorn', 'robocop', 'r2d2', 'c3po', 'neo', 'wolverine', 'thanos', 'pikachu']

#Variavel que pega a palvra da lista randomica
palavra = random.choice(palavras)

#lista de acertos
acertos = []

#Adiciona letra em palvra
for letra in palavra:
    acertos.append('_')

#Loop principal do jogo:
tentativas = 6
while tentativas > 0: 
    print("\nPalavra: ", " ".join(acertos))
    letra = input("Digite uma letra: ")

    if letra in palavra:
        print("Letra certa!")
        # Substitui o "_" pela letra correta nas pasições adequadas
        for i in range(len(palavra)):
            if palavra[i] == letra:
                acertos[i] = letra
    else:
        print("Letra errada, tente de novo!")
        tentativas -= 1
        print("Você ainda tem", tentativas, "tentativas")
    
    if '_' not in acertos:
        print("parabnéns vc ganhou!")
if tentativas == 0:
    print("Você perdeu a palavra era", palavra)        