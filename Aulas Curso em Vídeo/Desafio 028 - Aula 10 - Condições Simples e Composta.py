# Dentro das condições simples e compostas temos o if e else, essas condições precisam estar identadas para funcionarem. Sua escrita segue a estrutura abaixo:
# if carro.esquerda():
#     bloco True
# else:
#     bloco False

# tempo = int(input('Quanto tempo tem o seu carro? '))
# print('Seu carro está novinho!' if tempo <=3 else 'Seu carro já não é tão novo assim!')
# print('--Fim--')

#Obs.: Todo comando sem identação ser executado sempre, os comandos com identação poderão ser executados ou não.
# nome = str(input('Qual é o seu nome? '))
# if nome == 'Cesar':
#     print('Nossa, que nome bonite você tem!')
# print(f'Tenha um bom dia {nome}!')

# n1 = float(input('Digite a primeira nota: '))
# n2 = float(input('Digite a segunda nota: '))
# media = (n1+n2)/2
# print(f'Sua média ficou em: {media:.2f}')
# if media >=6:
#     print('Você ficou acima de 6.00, PARABÉNS!!!')
# else:
#     print('Você ficou abaixo de 6.00, infelizmente você não alcançou a nota necessária.')
          
from random import randint

adivinha = int(input('Nosso programa pensará em um número de 0 a 5, tente adivinhar em qual número ele pensará! Digite seu número aqui: '))
n = randint(0,5)
print(f'O número pensando foi: {n}')
if adivinha == n:
    print('Parabéns você acertou!')
else:
    print('Que pena você errou!')