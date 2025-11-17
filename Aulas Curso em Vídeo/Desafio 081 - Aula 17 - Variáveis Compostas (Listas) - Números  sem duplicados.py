lista = []
condição = 's'

while True:
    if condição == 's':
        valor = int(input('\nDigite um valor: '))
        lista.append(valor)
        condição = str(input('\nVocê gostaria de continuar [S/N]: ')).lower()
        
    else:
        print('\nVocê escolheu encerrar o programa.')

        break

if len(lista) == 1:
    print(f'\nVocê digitou apenas o valor {valor} !!!')

else:
    print(f'\nForam digitados {len(lista)} valores !!!')

lista.sort(reverse=True)

print(f'\nSua lista ficou assim: {lista}')


posição = [posição for posição, valor in enumerate(lista) if valor == 5]

if posição == []:
    print('\nO valor 5 não consta na sua lista.')

else: 
    print(f'\nO valor 5 está na lista na posição {posição} !!')
