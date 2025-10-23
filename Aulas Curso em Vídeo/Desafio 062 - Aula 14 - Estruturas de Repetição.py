print('Calculadora de P.A')
termo = int(input('\nDigite seu primeiro termo: '))
razao = int(input('\nDigite a razão desejada: '))
contadortotal = 0
numtermos = int(input('\nDigite a quantidade de termos que você quer ver: '))
while True
    contadortotal < numtermos:
    pa = termo + razao * contadortotal
    contadortotal += 1
    print(pa)
    # contador = 0
    # maistermos = int(input('Você gostaria de ver mais quantos termos? '))
    # while contador < maistermos:
    #     print(maistermos)
    #     contador += 1 
    # # # contador = 0
    # # while maistermos < contador:
    # #     pa = pa + razao * contador
    # #     contador += 1
    # #     print(pa)