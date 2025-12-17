print('-' * 60)
nome = 'LOJA SUPER BARATÃO'
print(f'{nome:^60}')
print('-' * 60)

while True:

    produto = str(input('Nome do Produto: '))

    preço = float(input('Preço: ').replace(',' , '.'))

    ação = ''
    
    while ação not in ('s' , 'n'):
        ação = str(input('Quer continuar? [S/N]: ')).lower().strip()[0]
        if ação == 'n':
            break

