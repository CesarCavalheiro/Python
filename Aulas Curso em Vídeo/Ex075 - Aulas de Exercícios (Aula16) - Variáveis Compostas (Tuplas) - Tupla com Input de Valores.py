num = (int(input('Digite o 1º Valor: ')),
       int(input('Digite o 2º Valor: ')),
       int(input('Digite o 3º Valor: ')),
       int(input('Digite o 4º Valor: ')))


print(f'\nOs valores digitados foram {num}.')

nove = num.count(9)

if nove == 0:
    print('\nNão foi digitado nenhum número 9.')

elif nove == 1:
    print('\nO número 9 aparece apenas 1 vez.')

else:         
    print(f'\nO número 9 aparece {nove} vezes.')

if 3 not in num:
    print('\nNão foi digitado nenhum número 3.')
    
else: 
    print(f'\nO valor 3 foi digitado primeiramente na posição {num.index(3)+1}')

cont = 0

for n in num:
    if n % 2 == 0:
        cont += 1

if cont == 0:
    print('\nNão foram digitados números pares.')

elif cont == 1:

    print(f'\nFoi digitado apenas 1 número par, o número {n}.')

else:
    print(f'\nForam digitados {cont} números pares.')


print('\n' * 3)