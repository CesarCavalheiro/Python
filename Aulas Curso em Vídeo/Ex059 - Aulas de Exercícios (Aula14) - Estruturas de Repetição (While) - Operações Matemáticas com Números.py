opção = '' 

n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))

while opção != 5:

    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')

    opção = int(input('\n>>>>> Qual é a sua opção? '))

    if opção == 1:
        print(f'A soma entre {n1} e {n2} é {n1+n2}')
        print('=-='*10)

    elif opção == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1*n2}')
        print('=-='*10)

    elif opção == 3:
        print(f'O maior entre {n1} e {n2} é {max(n1,n2)}')
        print('=-='*10)

    elif opção == 4:
        n1 = int(input('Novo primeiro Valor: '))
        n2 = int(input('Novo segundo Valor: '))

    elif opção == 5:
        print('Saindo do programa!!!')

    else:
        print('Opção Inválida, tente novamente!')