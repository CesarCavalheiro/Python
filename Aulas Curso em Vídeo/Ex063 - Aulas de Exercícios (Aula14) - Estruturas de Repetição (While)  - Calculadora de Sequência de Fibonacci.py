print('-'*30)
print('SEQUENCIA DE FIBONACCI')
print('-'*30)

termos = int(input(f'\nQuantos termos você quer mostrar? '))

n0 = 0
n1 = 1

print('~'*30)

print(f'{n0} -> {n1} -> ' , end='')

while termos - 2 > 0:

    fibo = n0 + n1

    termos -= 1

    print(F'{fibo} -> ' , end='')
    
    n0 = n1
    n1 = fibo

print('FIM')

print('~'*30)
   
   