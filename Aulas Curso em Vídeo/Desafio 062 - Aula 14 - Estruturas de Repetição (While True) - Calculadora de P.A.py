print('Calculadora de P.A')
termo = int(input('\nDigite seu primeiro termo: '))
razao = int(input('\nDigite a razão desejada: '))
numtermos = int(input('\nDigite a quantidade de termos que você quer ver: '))
contador = 0

while True:

    while numtermos > contador:
        pa = termo + razao * contador
        contador += 1
        print(pa)
    
    maistermos = int(input('Você gostaria de mostrar mais quantos termos? '))
    if maistermos == 0:
        print('\nVocê escolheu não mostrar mais termos, encerrando o programa!')
        break
    numtermos += maistermos

print('\nPrograma Encerrado com Sucesso!')