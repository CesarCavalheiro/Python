from datetime import date
nascimento = int(input('Qual é o ano do seu nascimento: '))
ano = date.today().year
if ano - nascimento < 18:
    print(f'Você tem {ano - nascimento}, ainda faltam {18 - (ano - nascimento)} anos para você se alistar!')
elif ano - nascimento == 18:
    print(f'Você tem {ano - nascimento}, Você deve se alistar esse ano!!')
else:
    print(f'Você tem {ano - nascimento}, já passou {(ano - nascimento) - 18} do seu alistamento!')