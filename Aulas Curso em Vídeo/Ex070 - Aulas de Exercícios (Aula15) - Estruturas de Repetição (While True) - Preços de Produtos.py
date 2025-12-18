print('-' * 60)
nome = 'LOJA SUPER BARATÃO'
print(f'{nome:^60}')
print('-' * 60)

cont = 0
lista = []
lista1 = []
total = 0
nomebarato = ''
valor = ''

while True:

    produto = str(input('\nNome do Produto: '))

    preço = float(input('Preço: R$ ').replace(',' , '.'))

    ação = ''

    total = total + preço

    if preço > 1000:
        cont += 1
    
    
    lista.append(preço)
    min(lista)

    if valor == min(lista):
        nomebarato = produto
    
    while ação != 's' and ação != 'n':
        ação = str(input('\nQuer continuar? [S/N]: ')).lower().strip()[0]

    if ação == 'n':
        break

print('-' * 16, ' FIM DO PROGRAMA ' , '-'*16)
print(f'O total da compra foi de R$ {total:.2f}')
print(f'Temos {cont} produtos custando mais de R$ 1000,00')
print(f'O produto mais barato foi {nomebarato} que custa R$ {min(lista):.2f}. ')
