print('Calculadora de P.A')
termo = int(input('\nDigite o termo: '))   
razao = int(input('\nDigite a razão: '))
nt = int(input('\nVocê gostaria de mostrar quantos termos? '))
contador = 1
print(f'Seu termo é: {termo}, sua razão é: {razao}, a quantidade de termos a ser mostrados é: {nt}, sua P.A. ficará assim: ')
while contador < nt+1:
    pa = termo + razao * contador
    contador += 1
    print(pa)



