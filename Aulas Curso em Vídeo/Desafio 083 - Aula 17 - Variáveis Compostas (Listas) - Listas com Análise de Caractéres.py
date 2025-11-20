expressão = input('\nDigite sua expressão matemática: ')

lista = []
cont = 0

for caractere in expressão:
    if caractere in '()':
        lista.append(caractere)
        cont += 1

if cont % 2 == 0:
    print('\nSua expressão está correta!')

else:
    print('\nSua expressão está errada!!!')