lista = []
listapar = []
listaimpar = []


while True:
    
    valor = int(input('\nDigite um valor [ou 999 para sair]: '))

    if valor == 999:
        print('\nEncerrando o programa.')

        print('\nPrograma Encerrado!!!')
        break

    lista.append(valor)

    if valor % 2 == 0:
        listapar.append(valor)
            
    else:
        listaimpar.append(valor)

print(f'\nA lista com seus números pares ficou assim: {listapar}')

print(f'A lista com seus números ímpares ficou assim: {listaimpar}')

print(f'Sua lista geral ficou assim: {lista}')

