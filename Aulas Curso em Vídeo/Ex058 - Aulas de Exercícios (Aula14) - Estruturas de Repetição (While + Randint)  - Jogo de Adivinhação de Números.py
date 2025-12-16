from random import randint
NumJogador = ''
cont = 0

print('\nOla!! Sou o seu computador...')
print('\nAcabei de pensar em um número entre 0 e 10.')
print('\nSerá que você consegue adivinhar qual é? ')

NumPc = randint(0 , 10)

while NumPc != NumJogador:

    cont += 1

    NumJogador = int(input('\nQual é o seu palpite? '))

    if NumJogador < NumPc:
        print('\nMais... Tente mais uma vez.')

    elif NumJogador > NumPc: 
        print('\nMenos... Tente mais uma vez.')

    elif NumJogador == NumPc and cont == 1:
        print(f'\nVocê acertou de primeira Parabéns!!!')
        break

    else: 
        print(f'\nVocê acertou, mas para isso precisou de {cont} tentativas!!!')
        break
