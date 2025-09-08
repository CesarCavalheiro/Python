valor = float(input('Digite o valor do produto: '))
condicao = int(input('Condição de pagamento: \nPara À vista, digite 1 \nPara Cartão, digite 2 \nPara 2x, Digite 3 \nPara 3 ou mais vezes, Digite 4 \nDigite aqui: '))
if condicao == 1:
    print(f'Para a condição à vista o produto fica com 10% de desconto. Valor total do produto {valor * 0.90:.2f}.')
elif condicao == 2:
    print(f'Para a condição à vista no cartão o produto fica com 5% de desconto. Valor total do produto R$ {valor * 0.95:.2f}.')
elif condicao == 3:
    print(f'Para a condição em 2x não há desconto. Valor total do produto R$ {valor:.2f}.')
else:
    print(f'Para as condições em 3x ou mais há 20% de acréscimo. Valor total do produto R$ {valor * 1.2:.2f}.')