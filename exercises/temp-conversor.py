def cel_to_fah(cel):
    fah =  (cel * 9/5) + 32
    return fah

def fah_to_cel(fah):
    cel = (fah - 32) * 5/9
    return cel

escolha = input("Sua temperatura está em cel ou fah?")
temp = int(input("Informe a temperatura: ") )

if escolha == 'cel':
    print("A temperatura", temp, "em Fahrenheit fica: ", cel_to_fah(temp) )
elif escolha == 'fah':
            print("A temperatura", temp, "em Celcius fica: ", fah_to_cel(temp) )
else:
      print("Escolha inválida.")


