from random import randint
from time import sleep
print('--=' * 40)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar em que número eu pensei...')
print('--=' * 40)
numero = int(input('Qual número você acha que pensei? '))
pensado = randint(0,5)
print('PROCESSANDO...')
sleep(3)
if  (pensado == numero):
    print(f'Uau você acertou! Eu pensei exatamente em {numero}!')
else:
    print(f'Ganhei! Eu pensei no número {pensado} e não no número {numero}!')