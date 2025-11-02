valor = float(input('Digite o valor do produto: ').replace(',','.'))
condicao = int(input('''Condição de pagamento: 
\nPara À vista, digite 1 
\nPara Cartão, digite 2 
\nPara 2x, Digite 3 
\nPara 3 ou mais vezes, Digite 4 
\nDigite aqui a condição de pagamento escolhida: '''))
if condicao == 1:
    print(f'\nPara a condição à vista o produto fica com 10% de desconto. Valor do desconto R$ {valor - valor*0.9:.2f}. Valor total do produto {valor * 0.90:.2f}.')
elif condicao == 2:
    print(f'\nPara a condição à vista no cartão o produto fica com 5% de desconto. Valor do desconto R$ {valor - valor*0.95:.2f}. Valor total do produto R$ {valor * 0.95:.2f}.')
elif condicao == 3:
    print(f'\nPara a condição em 2x não há desconto. Valor total do produto R$ {valor:.2f} em duas parcelas de R${valor / 2:.2f}.')
else:
    print(f'\nPara as condições em 3x ou mais há 20% de acréscimo. Valor total do acréscimo R$ {valor * 1.2 - valor:.2f}. Valor total do produto R$ {valor * 1.2:.2f}.')
    if condicao == 4:
        
        parcela = int(input('\nDigite a quantidade de parcelas que deseja pagar: '))

        print(f'\nSuas parcelas ficarão no valor de R$ {valor * 1.2 / parcela:.2f}')

    elif parcela == 3:
        print(f'\nSuas parcelas ficarão no valor de R$ {valor * 1.2 / parcela:.2f}')

    elif parcela == 4:
        print(f'\nSuas parcelas ficarão no valor de R$ {valor * 1.2 / parcela:.2f}')
    
    elif parcela == 5:
        print(f'\nSuas parcelas ficarão no valor de R$ {valor * 1.2 / parcela:.2f}')

    elif parcela == 6:
        print(f'\nSuas parcelas ficarão no valor de R$ {valor * 1.2 / parcela:.2f}')

    elif parcela == 7:
        print(f'\nSuas parcelas ficarão no valor de R$ {valor * 1.2 / parcela:.2f}')

    elif parcela == 8:
        print(f'\nSuas parcelas ficarão no valor de R$ {valor * 1.2 / parcela:.2f}')

    elif parcela == 9:
        print(f'\nSuas parcelas ficarão no valor de R$ {valor * 1.2 / parcela:.2f}')

    elif parcela == 10:
        print(f'\nSuas parcelas ficarão no valor de R$ {valor * 1.2 / parcela:.2f}')

    elif parcela == 11:
        print(f'\nSuas parcelas ficarão no valor de R$ {valor * 1.2 / parcela:.2f}')

    elif parcela == 12:
        print(f'\nSuas parcelas ficarão no valor de R$ {valor * 1.2 / parcela:.2f}')


    