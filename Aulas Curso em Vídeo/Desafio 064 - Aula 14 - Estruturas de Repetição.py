print('Calculadora de numeros aleatórios!')
n = 0
n1 = 0
contador = 0
while n != 999:
    n = int(input('\nDigite o número que você deseja somar ou 999 para encerrar o programa: '))
    n1 = n1 + n
    contador += 1
print(f'\nVocê digitou {contador-1} numeros, e o somatório de todos eles deu {n1-999}.')