valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual é o seu salário? '))
prazo = int(input('Em quanto tempo você pretende pagar? '))
parcela = salario * 0.30
if valor / prazo > parcela:
    print('Financiamento negado!!') 
    print('Valor da parcela excede 30% do valor do Salário')
elif parcela * prazo < valor:
    print('Financiamento reprovado!! Somatório do valor das parcelas menor que o valor do imóvel!!')
elif valor/prazo > parcela:
    print('Financiamento reprovado!! Infelizmente o valor da parcela que você pode pagar não é suficiente para pagar o imóvel!')
else:
    print('Parabéns financiamento aprovado!!')

