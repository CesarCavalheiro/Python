print ('-='*20)
print('Confederação Nacional de Natação')
print('-='*20)
print('Formulário para definição de categoria')
idade = int(input('Digite a sua Idade: '))
if idade <= 9:
    print('Você é da categoria MIRIM')
elif 10<= idade <= 14:
    print('Você é da categoria INFANTIL')
elif 14<= idade <= 19:
    print('Você é da categoria JUNIOR')
else:
    print('Você é da categoria Master')