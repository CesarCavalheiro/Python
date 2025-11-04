n = int(input('Digite um número qualquer: '))
contador = 0
for i in range(1,n+1):
    print(i, end=(' '))
    if n % i == 0:
        contador += 1
        print(f'O número foi divisível {contador} vezes!')
    