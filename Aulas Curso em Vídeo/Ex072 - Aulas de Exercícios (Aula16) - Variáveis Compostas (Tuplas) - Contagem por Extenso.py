extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

while True:

    n = int(input('Digite um número entre 0 e 20: '))

    if n == 999:
        break   


    if n < 0 or n > 20:
        print('ATENÇÃO!!! Seu número está fora do intervalo entre 0 e 20.')

    else:
        print(f'Você digitou' , {extenso[n]})

   
