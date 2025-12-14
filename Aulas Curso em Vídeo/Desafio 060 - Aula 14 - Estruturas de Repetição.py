# print('Calculadora de fatorial')
# n = int(input('\nDigite seu número '))
# fatorial = 1
# for c in range(1,n+1):
#     fatorial *= c
#     print(fatorial)
# print(f'O fatorial de {n} é {fatorial}')

# Acima vimos como fazer com FOR, agora vamos tentar com WHILE.

print('Calculadora de fatorial')
n = int(input('\nDigite seu número '))
num = n
fatorial = 1
while n > 0:
    fatorial *= n
    n -= 1

print(f'O fatorial de {num} é {fatorial}')

