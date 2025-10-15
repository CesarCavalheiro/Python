n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0

while opção != 5:
    print('Escolha:')
    print('\n1 Somar \n2 Multiplicar \n3 Mostrar o Maior \n4 Digitar novos numeros \n5 Sair do programa.')

    opção = int(input('\nDigite sua opção: '))
    
    if opção == 1:
        print(f'A soma dos seus números é: {n1 + n2}')
    
    elif opção == 2:
        print(f'A multiplicação dos seu numeros é: {n1 * n2}')
    
    elif opção == 3:
        print(f'O maior entre seus números é: {max(n1 ,n2)}') 
    
    elif opção == 4:
        print('\nDigite novos números')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opção == 5:
        print('Saindo do programa....')
    else:
        print('Opção inválida, tente novamente!')

print('Programa encerrado com sucesso!')
