lista = []

while True:

    valor = int(input('\nDigite um valor: '))
    if valor in lista:
        print('\nValor duplicado, não será acrescentado.')

    else:
        lista.append(valor)
        print('\nValor adicionado com sucesso!!!')
   

    opção = str(input('\nDeseja continuar? [S/N] '))

    if opção in 'Ss':
        print()

    else:
        print()
        break

print('=-' * 20)
    


print(f'\nA lista digitada foi: {sorted(lista)}')
