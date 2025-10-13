from random import randint

ntentativa = 0
n = randint(0,10)
tentativa = int(input('Digite um número de 0 a 10 e tente adivinhar em qual número o computador pensou: '))
while n != tentativa:
    tentativa = int(input(f'Você digitou {tentativa}. Você errou, tente novamente, digite um número diferente: '))
    ntentativa += 1
print(f'O computador escolheu {n}, você digitou {tentativa}. Você precisou de {ntentativa} tentativas, mas acertou, parabéns!')
    


#https://www.youtube.com/watch?v=LH6OIn2lBaI