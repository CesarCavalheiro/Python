numero = int(input('Digite o número que você deseja converter: '))
opçao = int(input('Digite: \n1 para decimal \n2 para octal \n3 para hexadecimal: '))
if opçao == 1:
    print(bin(numero))
elif opçao == 2:
    print(oct(numero))
else:
    print(hex(numero))