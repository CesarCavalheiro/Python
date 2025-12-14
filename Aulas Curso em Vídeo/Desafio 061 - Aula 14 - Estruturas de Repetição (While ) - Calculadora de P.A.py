print('Calculadora de P.A')
termo = int(input('\nDigite seu primeiro termo: '))
razao = int(input('\nDigite a razão desejada: '))
contador = 0
numtermos = int(input('\nDigite a quantidade de termos que você quer ver: '))
while contador < numtermos:
    pa = termo + razao * contador
    contador += 1
    print(pa)

   