print('-' * 60)
nome = 'LOJA SUPER BARATÃO'
print(f'{nome:^60}')
print('-' * 60)

cont = cont1000 = cont100 = total = 0

while True:

    produto = str(input('\nNome do Produto: '))

    preço = float(input('Preço: R$ ').replace(',' , '.'))

    ação = ''

    cont += 1

    #valor mais barato

    if cont == 1:
        maior = menor = preço
        nomebarato = produto
        nomemaior = produto

    else:
        if preço < menor:
            menor = preço
            nomebarato = produto

    #valor mais caro
    
        if preço > maior:
            maior = preço
            nomemaior = produto

    total += preço

    if preço > 1000:
        cont1000 += 1

    if preço < 100:
        cont100 += 1

    
    while ação != 's' and ação != 'n':
        ação = str(input('\nQuer continuar? [S/N]: ')).lower().strip()[0]

    if ação == 'n':
        break

print('-' * 16, ' FIM DO PROGRAMA ' , '-'*16)
print(f'O total da compra foi de R$ {total:.2f}')
print(f'Temos {cont1000} produtos custando mais de R$ 1000,00')
print(f'O produto mais barato foi {nomebarato} que custa R$ {menor:.2f}. ')
print(f'O produto mais caro foi {nomemaior} que custa R$ {maior:.2f}. ')
print(f'O valor médio dos produtos é R$ {total/cont:.2f}.')

#valores abaixo de 100

if cont100 == 0:
    print('Não há produtos com valor abaixo de R$ 100,00')

elif cont100 == 1:
    print('Há somente um produto com valor abaixo de R$ 100,00')

else:
    print(f'Foram comprados {cont100} produtos com valores abaixo de R$ 100,00.')
