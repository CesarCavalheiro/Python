reta_a = float(input('Digite o valor da sua primeira reta a qual chamaremos de reta \'A\': '))
reta_b= float(input('Digite o valor da sua segunda reta a qual chamaremos de reta \'B\': '))
reta_c = float(input('Digite o valor da sua terceira reta a qual chamaremos de reta \'C\': '))
if ((reta_a + reta_b > reta_c) and (reta_a + reta_c > reta_b) and (reta_b + reta_c > reta_a)):
    print('Suas 3 retas formam um triângulo!')
else:
    print('Suas 3 retas não formam um triângulo!')