n1 = int(input('Digite o primeiro número: '))
n2 = int(input('\nDigite o segundo número: '))
soma = 0
contador = 0
for c in range(n1, n2, 2):
    if c%3 == 0:
        contador += 1
        soma = soma + c
print(f'\nA quantidade de número ímpares multiplos de 3 são, {contador}.')
print(f'\nA soma de todos esses números da um total de: {soma}')