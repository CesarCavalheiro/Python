from random import randint
print('-='*20)
print('               JOKEMPÔ')
print('-='*20)
jogador = int(input('Escolha a sua jogada: \n1 para pedra \n2 para papel \n3 para tesoura \nDigite aqui sua escolha: '))
maquina = randint(1, 3)
if jogador == 1 and maquina == 1:
    print('Ambos escolheram Pedra! Essa rodada deu empate!!')
elif jogador == 2 and maquina == 2:
    print('Ambos escolheram Papel! Essa rodada deu empate!!')
elif jogador == 3 and maquina == 3:
    print('Ambos escolheram Tesoura! Essa rodada deu empate!!')
elif jogador == 1 and maquina == 2:
    print('Você escolheu pedra, a máquina escolheu papel! Papel enrola a pedra, a máquina ganhou!!')
elif jogador == 2 and maquina == 1:
    print('Você escolheu papel, a máquina escolheu pedra! Papel enrola a pedra, você ganhou!!')    
elif jogador == 1 and maquina == 3:
    print('Você escolheu pedra, a máquina escolheu tesoura! a pedra amassa a tesoura, você ganhou!!')
elif jogador == 3 and maquina == 1:
    print('Você escolheu tesoura, a máquina escolheu pedra! Pedra amassa a tesoura, a máquina ganhou!!')
elif jogador == 3 and maquina == 2:
    print('Você escolheu tesoura, a máquina escolheu papel! A tesoura corta o papel, a máquina ganhou!!')    
elif jogador == 2 and maquina == 3:
    print('Você escolheu papel, a máquina escolheu tesoura! A tesoura corta o papel, a máquina ganhou!!')    