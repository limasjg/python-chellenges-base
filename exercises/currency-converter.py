def real_dolar(real):
    dolar = real / 5
    return dolar

def real_euro(real):
    euro = real / 5.40
    return euro


moeda = input('Informe qual sua moeda: ')

valor = float(input('Informe o valor para conversão: '))

if moeda == 'real':
    print(f'Com {valor} em reais você terá {real_dolar(valor):.2f} em Dolar e em Euro {real_euro(valor):.2f}')
else:
    print('Moeda não reconhecida')