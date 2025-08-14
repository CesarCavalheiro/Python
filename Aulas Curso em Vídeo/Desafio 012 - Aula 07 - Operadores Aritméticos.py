preço = float(input('Digite o valor do produto: '))
desconto = float(input('Digite o valor do desconto concedido: '))
print(f'O valor original do produto é {preço:.2f}, considerando o desconto de {desconto:.2f}% o valor a pagar fica: {preço*(1-(desconto/100)):.2f}')