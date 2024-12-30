materias = int(input("Quantas máterias?: "))

notas = []

for i in range(materias):
    nota = float(input(f'Digite sua nota {i}: '))
    notas.append(nota)

sum_notas = sum(notas)
media = sum_notas / materias

print(f'Sua média de {materias} notas é {media:.1f}')
'''print("---------- Calculadora de Notas --------")   

nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a nota matéria 1: ") )
nota2 = float(input("Digite a nota matéria 2: ") )
nota3 = float(input("Digite a nota matéria 3: ") )

media = (nota1 + nota2 + nota3) / 3

print(f'O aluno {nome} ficou com a média {media:.1f}')'''
