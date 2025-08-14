salario = float(input('Qual seu salário atual: '))
aumento = float(input('Quanto você ganhou de aumento? '))
print(f'Seu salário é de R${salario:.2f}, com o aumento de {aumento:.2f}% seu novo salário passa a ser {((1+(aumento/100))*salario):.2f}')