cont = 1
pares = 0
lista = []
par = []

for v in range(1,5):
    valor = int(input(f'\nDigite seu {cont}º valor: '))
    cont += 1

       
    if valor % 2 == 0:
        par.append(valor)
        pares += 1

    else:
        nopares = ('Não foram digitados valores pares')


    lista.append(valor)
    tupla = tuple(lista)
    

print(f'\nVocê digitou os valores: {tupla}')


print('\nForam digitados',tupla.count(9),'numero(s) 9')

if 3 not in tupla:

    print('\nO valor 3 não foi digitado em nenhuma posição')

else:

    print(f'\nO número 3 tem sua primeira aparição na {tupla.index(3)+1}ª posição')

if pares == 0:

    print(f'\n{nopares}')

else:

    print(f'\nOs valor(es) par(es) digitados foi(ram)',end=' ')
    print(*par)


    


print()
print()
print()