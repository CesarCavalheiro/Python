print('-=' * 10) 
print('Calculadora de P.A')
print('-=' * 10) 

termo = int(input('\nDigite o termo: '))

razão = int(input('\nDigite a razão '))
print()

cont = 0

while cont < 10:

    print(f'{termo} -> ' , end='')

    cont += 1

    termo += razão

print('PAUSA')

while True:

    mais = int(input('\nQuantos termos a mais você quer mostrar? '))
    print()

    nmais = mais

    if nmais == 0:
        print(f'Progressão finalizada com {cont} termos mostrados.')

        print()
        print()
        print()

        break

    while mais > 0:

        mais -= 1

        print(f'{termo} ->' , end=' ')

        cont += 1

        termo += razão

    print('PAUSA')

    


