from random import randint
print('*** Pedra, Papel e Tesoura ***')

n1 = 'Pedra'
n2 = 'Papel'
n3 = 'Tesoura'

print('''Escolha:
\n1 para Pedra
\n2 para Papel
\n3 para Tesoura''')
contadorjogador = 0
contadorpc = 0

while True:

    escolha = int(input('\n\033[32mDigite sua escolha: \033[m'))
    pc = randint(1,3)

    if escolha == 1 and pc == 1:
      print(f'\nVocê escolheu Pedra e o pc escolheu Pedra, ninguém marcou ponto!')

    elif escolha == 2 and pc == 2:
      print(f'\nVocê escolheu Papel e o pc escolheu Papel, ninguém marcou ponto!')
    
    elif escolha == 3 and pc == 3:
      print(f'\nVocê escolheu Tesoura e o pc escolheu Tesoura, ninguém marcou ponto!')
    
    elif escolha == 1 and pc == 2:
      print(f'\nVocê escolheu Pedra e o pc escolheu Papel!')
      print(f'\nPapel enrola pedra, o computador ganhou essa! ')
      contadorpc += 1
      print(f'''\nO computador está com: {contadorpc} pontos!
Você está com {contadorjogador} pontos!''')

    elif escolha == 2 and pc == 1:
      print(f'\nVocê escolheu Papel e o pc escolheu Pedra!')
      print(f'\nPapel enrola pedra, o você ganhou essa! ')
      contadorjogador += 1
      print(f'''\nO computador está com: {contadorpc} pontos!
Você está com {contadorjogador} pontos!''')
    
    elif escolha == 2 and pc == 3:
      print(f'\nVocê escolheu Papel e o pc escolheu Tesoura!')
      print(f'\nTesoura corta Papel, o computador ganhou essa! ')
      contadorpc += 1
      print(f'''\nO computador está com: {contadorpc} pontos!
Você está com {contadorjogador} pontos!''')

    elif escolha == 3 and pc == 2:
      print(f'\nVocê escolheu Tesoura e o pc escolheu Papel!')
      print(f'\nTesoura corta Papel, o você ganhou essa! ')
      contadorjogador += 1
      print(f'''\nO computador está com: {contadorpc} pontos!
Você está com {contadorjogador} pontos!''')
       
    elif escolha == 3 and pc == 1:
      print(f'\nVocê escolheu Tesoura e o pc escolheu Pedra!')
      print(f'\nPedra esmaga a Tesoura, o computador ganhou essa! ')
      contadorpc += 1
      print(f'''\nO computador está com: {contadorpc} pontos!
Você está com {contadorjogador} pontos!''')
       
    elif escolha == 1 and pc == 3:
      print(f'\nVocê escolheu Pedra e o pc escolheu Tesoura!')
      print(f'\nPedra esmaga a Tesoura, você ganhou essa! ')
      contadorjogador += 1
      print(f'''\nO computador está com: {contadorpc} pontos!
Você está com {contadorjogador} pontos!''')