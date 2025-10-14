n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
somar = n1 + n2
multiplicar = n1 * n2
maior = max(n1,n2)
print('Escolha: \n1 somar \n2 multiplicar \n3 maior \n4 novos números \n5 sair do programa')
opção = int(input('Digiteu sua opção: '))
if opção == 1:
    print(f'A soma dos seus números é: {somar}')
if opção == 2:
    print(f'A multiplicação dos seu numeros é: {multiplicar}')
if opção == 3:
    print(f'O maior entre seus números é: {maior}') 
if opção == 4:
    print('Digite novos números')
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))