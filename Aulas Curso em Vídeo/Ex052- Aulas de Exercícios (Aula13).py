n = int(input('Digite um número qualquer: '))
contador = 0

print()

for i in range(1,n+1):
    print(i, end=(' '))

if n % i == 0:
    contador +=1

if contador == 2:
    print(f'''\nO número {n} foi divisível {contador} vezes!
Por isso ele é primo!!!''')

else:
    print(f'\nO número {n} foi divisível {contador} vezes!')
    print(f'\nPor isso ele não é PRIMO!!!')
     
 