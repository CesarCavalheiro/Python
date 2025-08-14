preço = float(input('Digite o valor do seu produto: '))
desconto = float(input('Digite o valor do desconto: '))
print(f'O Valor do produto é: R${preço:.2f}, com o desconto de {desconto:.2f}%, o valor final fica em: R${(1-(desconto/100))*preço:.2f}')