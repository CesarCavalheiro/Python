from datetime import date
print('=== CONFEDERAÇÃO NACIONAL DE NATAÇÃO ===')
print('\nDefinição de categorias conforme idade!')
nasc = int(input('\nDigite o ano do seu nascimento: '))
anoAtual = date.today().year
idade = anoAtual - nasc
if idade <= 9:
    print(f'\nVocê tem {idade} anos, sua categoria é: MIRIM')

elif idade <= 14:
    print(f'\nVocê tem {idade} anos, sua categoria é: INFANTIL')

elif idade <= 19:
    print(f'\nVocê tem {idade} anos, sua categoria é: JUNIOR')

elif idade <= 25:
    print(f'\nVocê tem {idade} anos, sua categoria é: SÊNIOR')

else: 
    print(f'\nVocê tem {idade} anos, sua categoria é: MASTER')