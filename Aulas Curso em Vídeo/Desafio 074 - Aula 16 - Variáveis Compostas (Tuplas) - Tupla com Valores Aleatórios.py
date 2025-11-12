from random import randint

numeros = []

for c in range(0,5):
    
    random = (randint(0,100))
    
    numeros.append(random)

tupla = tuple(numeros)

print(f'\nAlistagem de números gerados de forma aleatória são: {tupla}')
   

print(f'\nDentre os números gerados, o menor é {min(tupla)} e o maior é {max(tupla)}')

print('')
print('')
print('')