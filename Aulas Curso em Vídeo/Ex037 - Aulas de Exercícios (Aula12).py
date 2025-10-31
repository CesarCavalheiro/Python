print('Calculadora de Conversão!')

n = int(input('\nDigite o número que você gostaria de converter: '))
base = int(input('\nEscolha uma das bases para converter o seu número: 1 para Binário, 2 para Octal e 3 para Hexadecimal: '))

if base == 1:
    print(f'O número {n} convertido para binário é {bin(n)[2:]}')
elif base == 2:
    print(f'O número {n} convertido para binário é {oct(n)[2:]}')
elif base == 3:
    print(f'O número {n} convertido para binário é {hex(n)[2:]}')
else:
    print('Você digitou uma opção inválida.')