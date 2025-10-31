print('Avaliador de empréstimo para a Casa Própria')
vcasa = float(input('\nQual é o valor da casa que você gostaria de comprar? R$ '))
salario = float(input('\nQual o valor do seu salário: R$ '))
prazo = int(input('\nEm quantos anos você prentende pagar? '))
salario30porcento = (salario/100)*30
parcela = vcasa / (prazo*12)
if parcela > salario30porcento:
    print(f'\nPara pagar uma casa no valor de {vcasa} em {prazo}, a parcela ficaria {parcela:.2f}')
    print(f'\nVocê só pode comprometer 30% do seu salário que equivale a R$ {salario30porcento}')
    print('\nComo o valor da parcela é maior que o valor que você pode comprometer o empréstimo foi NEGADO!!')
else:
    print(f'\nPara pagar uma casa no valor de {vcasa} em {prazo}, a parcela ficaria R$ {parcela:.2f}')
    print(f'\nVocê só pode comprometer 30% do seu salário que equivale a R$ {salario30porcento}')
    print('\nComo o valor da parcela é menor ou igual ao valor que você pode comprometer o empréstimo foi APROVADO!!')
    print('\nParabens!!!')