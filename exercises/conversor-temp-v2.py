def cel_to_fah(cel):
    fah = (cel * 9/5) + 32
    return fah

def cel_to_kel(cel):
    kel = cel + 273.15
    return kel

def fah_to_cel(fah):
    cel = (fah - 32) * 5/9
    return cel

def fah_to_kel(fah):
    kel = (fah -32) * 5/9 + 273.15
    return kel

def kel_to_cel(kel):
    cel = kel - 273.15
    return cel

def kel_to_fah(kel):
    fah = (kel - 273.15) * 9/5 + 32
    return fah

tipo= input('Informe sua tipo de medição: ')

temp = int(input('Digite a temperatura: '))

if tipo == 'cel':
    print('Sua temperatura em fahrenheint será: ', cel_to_fah(temp), 'e em Kelvin: ', cel_to_kel(temp))
elif tipo == 'fah':
    print(f'Sua temperatura em Celcius será: {fah_to_cel(temp):.1f}, e em Kelvin: {fah_to_kel(temp):.1f}')
elif tipo == 'kel':
    print(f'Sua temperatura em fahrenheit será: {kel_to_fah(temp):.1f}, e em Celcius: {kel_to_cel(temp):.1f}')
    
else:
    print('Erro!')