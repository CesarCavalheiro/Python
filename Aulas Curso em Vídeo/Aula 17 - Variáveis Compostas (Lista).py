from random import randint

copo = randint(1,3)

jogador = int(input('Escolha em qual dos 3 copos pode estar a bolinha: '))

if copo == jogador:
    print(f'Parabéns você escolheu o copo {jogador} e o pc botou a bolinha no copo {copo}')

else:
    print(f'Que pena, você errou. Você escolheu o copo {jogador} e o pc botou a bolinha no copo {copo}' )
    