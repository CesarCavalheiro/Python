print('Calculadora de P.A')

pa = int(input('\nDigite o primeiro termo: '))
razao = int(input('\nDigite a razão da P.A: '))
contador_total = 0
novostermos = 1

while True:
    novostermos = int(input('\nVocê gostaria de mais quantos termos? '))
    if novostermos == 0:
        print('\nVocê escolheu encerrar o programa.')
        print('\nEncerrado!!!')
        break
    contador = 0
    while contador < novostermos:
        termo = pa + razao * contador_total
        print(termo, end=' ')
        contador += 1
        contador_total += 1

    print()

#tentar arrumar o código abaixo

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
t = int(input('\nVocê gostaria de mostrar mais quantos termos? '))
if t != 0:
    termo = pa
    contador = 1
    while contador < t+1:
        pa = termo + razao * contador
        contador += 1
        print(pa)
    t = int(input('\nVocê gostaria de mostrar mais quantos termos? '))
else:
    print('Ok, Encerrado o programa!')
    print('Programa encerrado!')

