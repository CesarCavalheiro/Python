cont = n = 0
total = 0
while True:

    cont += 1

    n = int(input('Digite o valor para o somatório (Para sair digite 999): '))
    
    if n == 999:
        break

    total = n + total

print(f'A soma dos {cont-1} valores é igual a: {total:.2f}!')