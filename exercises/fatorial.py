def fatorial(num):
    if num <= 0:
        return "Erro! Não existe fatorial de zero ou número negativo."
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

num = int(input("Diigite um núemro inteiro para saber seu fatorial: "))
result = fatorial(num)
print("o Fatorial de", num, "é",result)