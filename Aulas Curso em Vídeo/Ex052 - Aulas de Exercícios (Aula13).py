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

preto_claro = '\033[90m'
vermelho_claro = '\033[91m'
verde_claro = '\033[92m'
amarelo_claro = '\033[93m'
azul_claro = '\033[94m'
magenta_claro = '\033[95m'
ciano_claro = '\033[96m'
branco_claro = '\033[97m'
reset = '\033[0m'

num = int(input('Digite seu número: '))
print( )
contador = 0

for c in range(1, num + 1):
    if num % c == 0:
        contador += 1
        print(vermelho_claro, end= '')
    else:
        print (reset, end='')
   
    print(f'{c} ', end='')
    
print( )
print (reset, end='')

if contador == 2:
    print(f'\nO número {num} foi divisível {contador} vezes!')
    print('Por isso ele é primo!!!')

else:
    print(f'\nO número {num} foi divisível {contador} vezes!')
    
    print(f'\nPor isso ele não é PRIMO!!!')