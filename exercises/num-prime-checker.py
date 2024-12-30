def eh_primo(num):
    if num <=1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True
    
print("------------ Verificador de número primo -----------\n")

num = int(input("Digite um número: "))

if eh_primo(num):
    print("O número", num, "é primo")
else:
    print("O número", num, "não é primo")
    

    