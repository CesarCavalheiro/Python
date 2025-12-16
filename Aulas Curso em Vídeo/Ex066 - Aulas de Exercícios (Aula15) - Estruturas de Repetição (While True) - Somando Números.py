cont = soma = 0

while True:

    n = int(input('Digite seu número [ou 999 para parar]: '))

    if n == 999:
        break

    cont += 1
    
    soma += n

print(f'Foram digitados {cont} numeros e a soma entre eles foi {soma}!')