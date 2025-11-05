# verde = '\033[32m'
# reset = '\033[0m'

# n = int(input('Digite um número qualquer: '))
# print()

# contador = 0

# for i in range(1, n +1):
#     if n % i == 0:
#         print(f'{verde}{i}{reset}', end=' ')
#         contador += 1
#     else:
#         print(i, end=' ')

# print( )

# if contador == 2:
#     print(f'\nO número {n} foi divisível {contador} vezes!')
#     print('Por isso ele é primo!!!')

# else:
#     print(f'\nO número {n} foi divisível {contador} vezes!')
#     print(f'\nPor isso ele não é PRIMO!!!')
     

# ESTUDAR ESSE JEITO DE FAZER

verde = '\032[034m'
reset = '\033[0m'

num = int(input('Digite seu número: '))

for c in range(1, num, + 1):
    if num % c == 0:
        print('\033[034m', end= '')
    else:
        print ('\033[m', end='')
    print(f'{c} ', end='')
      

