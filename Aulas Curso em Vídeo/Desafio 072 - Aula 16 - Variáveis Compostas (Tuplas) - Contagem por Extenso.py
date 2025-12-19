extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
vermelho = '\033[31m'
reset = '\033[0m'

while True:

    numero = int(input('\nDigite um número entre 0 e 20 [999 para parar]: '))

    if numero < 0 or numero > 20:
        print(f'\n{vermelho}Seu número está fora do intervalo entre 0 e 20, tente novamente!!{reset}')

    else:
        print ('\n Você digitou o número:',extenso[numero])


 