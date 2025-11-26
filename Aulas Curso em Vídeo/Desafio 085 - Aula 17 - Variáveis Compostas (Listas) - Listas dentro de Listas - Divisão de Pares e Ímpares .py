lista = []
pares = []
impares = []

cont = 1

for l in range(0,7):
    valores = int(input(f'Digite o {cont}º valor: '))

    lista.append(valores)

    cont += 1

    if valores % 2 == 0:
        pares.append(valores)
        pares.sort()

    else:
        impares.append(valores)
        impares.sort()

    print(f'\nOs valores pares digitados foram: {pares}')

    print(f'\nOs valores impares digitados foram: {impares}')