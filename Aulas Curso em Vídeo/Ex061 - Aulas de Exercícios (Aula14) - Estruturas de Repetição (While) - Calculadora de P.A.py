print('-=' * 10) 
print('Calculadora de P.A')
print('-=' * 10) 

termo = int(input('\nDigite o termo: '))

razão = int(input('\nDigite a razão '))
print()

termoinicial = termo

cont = 1

while cont <= 10:

    print(f'{termo} -> ' , end='')

    termo += razão

    cont += 1

print('Fim')

print()
print()
print()