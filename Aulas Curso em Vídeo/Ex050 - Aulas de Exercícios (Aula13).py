total = 0
contador = 0
for n in range(1,7):
    n = int(input(f'Digite seu {contador}º número: '))
    if n % 2 == 0:
        contador += 1
        total = n + total
print(f'\nVocê digitou um total de {contador} números pares. A soma dos números pares digitados é: {total}')