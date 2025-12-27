lista = []

for pos in range(0,5):
    numero = int(input('\nDigite seu número: '))
    if pos == 0:
        lista.insert(0 , numero)
        print(f'\nO número {numero} foi inserido no ínicio da lista.')

    else:

        pos = 0
        while pos < len(lista) and lista[pos] < numero:

            pos += 1

        lista.insert(pos, numero)
        print(f'\nO número {numero} foi inserido na posição {pos}.')

        print(f'\nSua lista está ficando assim {lista}.')


   