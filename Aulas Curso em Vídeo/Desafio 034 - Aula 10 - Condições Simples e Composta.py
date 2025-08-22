salario = float(input('Qual é o seu salário:' ))
if (salario<=1250):
    print(f'Seu aumento foi de 15%, seu novo salário será de R$ {salario*1.15:.2f}.')
else:
    print(f'Seu aumento foi de 10%, seu novo salário será de R$ {salario*1.10:.2f}.')