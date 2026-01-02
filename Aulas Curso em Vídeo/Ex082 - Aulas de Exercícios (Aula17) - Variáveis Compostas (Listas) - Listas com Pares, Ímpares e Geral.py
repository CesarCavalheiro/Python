lista = []
listapar = []
listaimpar = []

while True:
    lista.append(int(input('Digite um número: ')))

    opção = str(input('Quer continuar? [S/N] ').lower())

    while opção not in 'sn':
        opção = str(input('Quer continuar? [S/N] ').lower())
    
    if opção == 'n':
        break

for n in lista:
    if n % 2 == 0:
        listapar.append(n)

    else: 
        listaimpar.append(n)


print(f'\nSua lista completa é: {lista}')
print(f'\nA lista com os números pares é {listapar}')
print(f'\nA lista com os números ímpares é {listaimpar}')