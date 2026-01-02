lista = []
cont = 0


while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    #lista.sort(reverse=True)
    cont +=1

    opção = str(input('Quer continuar? [S/N]: ').lower())

    while opção not in 'sn':
        opção = str(input('Quer continuar? [S/N]: ').lower())
        
    if opção == 'n':
        break


print(f'\nVocê digitou {cont} números.')
print(f'\nOs valores em ordem decrescente são {sorted(lista, reverse=True)}')

#Na lista acima podemos ordenar de forma descrescente de duas maneiras:

# 1º fora do print ordenando a lista com o métido SORT fazendo um lista.sort(reverse=True)
# 2º no print co a função SORTED fazendo um sorted(lista, reverse=True)

if 5 in lista:
    print('\nO valor 5 faz parte da lista!')

else:
    print('\nO Valor 5 não faz parte da lista!')