# from math import factorial

# print('Calculadora de fatorial')

# n = int(input('Digite seu número: '))
# f = factorial(n)
# print(f'O fatorial de {n} é {f}!')

#Acima uma forma de fazer com a importação de módulos

print('Calculadora de fatorial')

n = int(input('\nDigite seu número: '))
print(f'\nCalculando o {n}!' ' =' , end=' ')

fatorial = 1

while n > 0:
    print(f'{n}', end=' ')
    print(' x ' if n > 1 else ' = ' , end= ' ')
   
    fatorial *= n
    n -= 1
    
print(f'{fatorial}')

print( )
print( )
print( )