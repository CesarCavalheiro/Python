print('Calculadora de P.A')
termo = int(input('\nDigite o primeiro termo: '))   
razao = int(input('\nDigite a razão: '))
n = razao
contador = 1
while contador < 11:
    pa = termo + razao
    razao = razao + n
    contador += 1
    print(pa)





