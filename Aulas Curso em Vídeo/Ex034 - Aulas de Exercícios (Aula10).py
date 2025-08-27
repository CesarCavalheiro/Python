salario = float(input('Digite seu salário atual: '))
if salario <= 1250:
    print(f'Seu aumento foi de 15%, seu novo salário é de R$ {salario*1.15}.')
else:
    print(f'Seu aumento foi de 10%, seu novo salário é de R$ {salario*1.10}.')