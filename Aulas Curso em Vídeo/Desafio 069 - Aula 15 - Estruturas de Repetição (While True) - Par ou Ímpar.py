from random import randint

p = ''
i = ''
vitoriajogador = 0
vitoriapc = 0

print('-=' * 60)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 60)

while True:

    jogador = int(input('\nDigiteu um número: '))
    parouimpar = str(input('\nVocê que par (P) ou Ímpar (I)? ')).lower()

    pc = randint(1, 10)


    if (jogador + pc) % 2 == 0 and parouimpar == 'p':
        print(f'\nVocê jogou {jogador} e o pc jogou {pc}. Como {jogador + pc} é par, Você ganhou!!!')
        vitoriajogador += 1
        
    
    if (jogador + pc) % 2 == 0 and parouimpar == 'i':
       print(f'\nVocê jogou {jogador} e o pc jogou {pc}. Como {jogador + pc} é par, o Pc ganhou!!!')
       vitoriapc += 1
       break

   
    if (jogador + pc) % 2 != 0 and parouimpar == 'i':
       print(f'\nVocê jogou {jogador} e o pc jogou {pc}. Como {jogador + pc} é ímpar, Você ganhou!!!')
       vitoriajogador += 1

    
    if (jogador + pc) % 2 != 0 and parouimpar == 'p':
        print(f'\nVocê jogou {jogador} e o pc jogou {pc}. Como {jogador + pc} é ímpar, o Pc ganhou!!!')
        vitoriapc += 1
        break

print(f'\nVocê teve um total de {vitoriajogador} vitoria(s), e o pc um total de {vitoriapc} vitoria(s).')    


print(' ')