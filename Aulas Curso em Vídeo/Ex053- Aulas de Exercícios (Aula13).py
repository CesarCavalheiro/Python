frase = str(input('Digite uma frase: '))
invert = frase[::-1]

if frase == invert:
    print(f'\nA frase {frase} fica igual {invert} quando lida de trás para frente, logo ela é um palindromo! ')

else:
    print(f'\nA frase {frase} fica igual {invert} quando lida de trás para frente, logo ela não é um palindromo! ')
