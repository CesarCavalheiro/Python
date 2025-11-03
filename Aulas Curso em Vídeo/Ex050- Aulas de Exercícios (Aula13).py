total = 0
contador = 1
for n in range(1,7):
    n = int(input(f'Digite seu {contador}º número: '))
    contador += 1
    if n % 2 != 0:
        total = n + total
print(f'\nA soma dos números ímpares digital é ?{total}')