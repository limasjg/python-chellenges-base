'''
palavra = input('Informe uma palavra: ')
invert = ''.join(reversed(palavra))
if palavra == invert:
    print('É Palindromo')
else:
    print('Não é Palindromo')
'''

def main():
    palavra = input('Informe uma palavra: ')
    palavra = palavra.replace(" ", "").lower()
    invertida = palavra[::-1]
    if palavra == invertida:
        print('É um palíndromo!')
    else:
        print('Não é um palíndromo.')

if __name__ == "__main__":
    main()