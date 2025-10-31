from datetime import date
print('Alistamento Militar!!!')
anoAtual = date.today().year
ano = int(input('\nQual é o ano do seu nascimento? '))
idade = anoAtual - ano
if idade > 18:
    print(f'\nVocê tem {idade} anos.')
    print(f'\nVocê já passou da idade de alistamento, você deveria ter se alistado há {idade-18} anos atrás.')
    print(f'\nSeu alistamento deveria ter sido em {ano + 18}')

elif idade == 18:
    print(f'\nVocê está com {idade} anos, este é o seu ano de alistamento!')

else:
    print(f'\nVocê tem {idade} anos. ')
    print(f'\nAinda faltam {18 - idade} anos para o seu alistamento.')
    print(f'\nSeu alistamento será em {ano + 18}')
    print('')