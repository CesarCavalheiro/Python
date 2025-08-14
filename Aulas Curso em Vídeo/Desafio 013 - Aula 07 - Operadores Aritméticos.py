salario = float(input('Digite o seu salário atual: '))
aumento = float(input('Digite o % de aumento recebido: '))
print(f'Seu salário atual é de: {salario:.2f}, seu novo salário considerando o aumento de {aumento:.2f}% será de {salario*(1+(aumento/100)):.2f}:')