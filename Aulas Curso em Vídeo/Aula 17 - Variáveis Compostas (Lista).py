lista = []

for i in range(0,5):
    valor = (int(input('\nDigite um valor: ')))

    if len(lista) == 0:

        lista.append(valor)

        print(f'\nO valor {valor} foi adicionado no início da lista.')

    else:
        pos = 0
 
        while pos < len(lista) and lista[pos] < valor:
                    
            pos += 1


        lista.insert(pos, valor)
        print(f'O valor {valor} foi inserido na posição {pos}:')
        print(lista)
        
print(f'A lista final ficou assim {lista}.')