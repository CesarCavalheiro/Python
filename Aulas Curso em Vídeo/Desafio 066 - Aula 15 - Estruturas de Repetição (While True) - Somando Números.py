cont = n = 0
total = 0
while True:
    n = int(input('Digite o valor para o somatório (Para sair digite 999): '))
    cont += 1
    if n == 999:
        break
    total = n + total
print(f'A soma dos {cont} valores é igual a: {total:.2f}!')