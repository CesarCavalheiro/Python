from random import randint

cont = contpc = 0


print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)

while True:

    jogador = int(input('Diga o seu valor: '))

    opção = str(input('\nPar, Ímpar ou Sair [P/I/S]: '))

    pc = randint(0,10)

    if (jogador + pc) % 2 == 0 and opção in 'Pp':

        print('-' * 30)
        print(f'Você jogou {jogador}, o computador {pc}. Total deu {jogador + pc} que é PAR')
        print('-' * 30)
        cont += 1 
        print('Você escolheu par e deu par... Você Ganhou!!!')
        print(f'\nForam Jogadas {cont+contpc} partidas e o placar está: {cont} para você x {contpc} para o pc')
        print('=-'*15)

    elif (jogador + pc) % 2 == 0 and opção in 'Ii':

        print('-' * 30)
        print(f'Você jogou {jogador}, o computador {pc}. Total deu {jogador + pc} que é PAR')
        print('-' * 30)
        contpc += 1 
        print('Você escolheu ímpar e deu par... Você Perdeu!!!')
        print(f'\nForam Jogadas {cont+contpc} partidas e o placar está: {cont} para você x {contpc} para o pc')
        print('=-'*15)
           
    elif (jogador + pc) % 2 != 0 and opção in 'Ii':

        print('-' * 30)
        print(f'Você jogou {jogador}, o computador {pc}. Total deu {jogador + pc} que é ÍMPAR')
        print('-' * 30)
        cont += 1 
        print('Você escolheu ímpar e deu impar... Você Ganhou!!!')
        print(f'\nForam Jogadas {cont+contpc} partidas e o placar está: {cont} para você x {contpc} para o pc')
        print('=-'*15)


    elif (jogador + pc) % 2 != 0 and opção in 'Pp':

        print('-' * 30)
        print(f'Você jogou {jogador}, o computador {pc}. Total deu {jogador + pc} que é ÍMPAR')
        print('-' * 30)
        contpc += 1 
        print('Você escolheu par e deu impar... Você Perdeu!!!')
        print(f'\nForam Jogadas {cont+contpc} partidas e o placar está: {cont} para você x {contpc} para o pc')
        print('=-'*15)

    elif opção in 'Ss':
        if cont + contpc == 0:
            print('\nPlacar zerado, você nem chegou a jogar!!!')
            break

        elif cont > contpc:
            print(f'\nParabéns!!! das {cont+contpc} partidas você ganhou {cont}.')
            print(f'\nPlacar final: Jogador {cont} x Pc {contpc}')
            break

        else:
            print(f'\nGAMER OVER!!! Das {cont+contpc} partidas o Pc ganhou {contpc}. ')
            print(f'\nPlacar final: Jogador {cont} x Pc {contpc}')
            break
