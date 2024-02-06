materias = int(input('Informe quantas matérias: '))

lista_notas = []

for i in range(materias):
    nota = float(input(f'Informe o valor da sua nota na matéria {i + 1}: '))
    lista_notas.append(nota)

soma_notas = sum(lista_notas)

media = soma_notas / materias

print(f'A média das suas {materias} matérias foi {media:.1f}')

