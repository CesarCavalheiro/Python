from random import randint

for c in range(0,5):

    random = (randint(0,100), randint(0,100), randint(0,100), 
              randint(0,100), randint(0,100))

print(f'A lista de números aleatórios gerada foi:' , end= ' ')    

for n in random:
    print(n, end=' ')

print()


print(f'O maior valor sorteado foi {max(random)}.')

print(f'O menor valor sorteado foi {min(random)}.')



