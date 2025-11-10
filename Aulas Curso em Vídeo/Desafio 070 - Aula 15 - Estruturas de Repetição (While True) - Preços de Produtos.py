print('=' * 40)
nome = ('LOJA BARATÃO DA ECONOMIA')
print(f'{nome:^40}')
print('=' * 40)

reset = '\033[0m'
verde = '\033[32m'

totalitem = 0
itens = 0
totalgasto = 0
valormaisque1000 = []
barato = []
produtos = []
nomebarato =''

continuar = ''

while True:
    produto = str(input(f'\nDigite o nome do produto: {verde}'))
    print(reset)

    produtos.append(produto)

    valor = float(input(f'\nDigite o valor do produto: {verde}').replace(',' , '.'))
    print(reset)
    totalitem += 1

    totalgasto = totalgasto + valor

        

    barato.append(valor)

    
    if valor == (min(barato)):
        nomebarato = produto
    

    if valor > 1000:
        valormaisque1000.append(valor)
        itens += 1 

        
    continuar = str(input(f'\nQuer continuar [S/N]: {verde}')).lower()
    print(reset)

    if continuar == 'n':
        break
        

print(f'\nVocê comprou {verde}{totalitem} item(ns){reset} com um valor total de {verde}R$ {totalgasto:.2f}{reset}')

print(f'\n{verde}{itens}{reset} desse(s) item(ns) tem um valor maior que {verde}R$ 1000,00{reset}' )

print(f'\nO produto mais barato da sua lista foi {verde}{nomebarato}{reset} com o valor de {verde}R$ {min(barato):.2f}{reset}')

print('')
print('')
print('')
