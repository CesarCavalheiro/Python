print('Calculadora de Fibonacci')

fibo = int(input('\nDigite a quantidade de número na sequência de Fibonacci que você quer ver: '))
n1 = 0
n2 = 1
contador = 0
while fibo > contador:
    sequencia1 = n1 + n2
    sequencia2 = (sequencia1 + 1) + sequencia1
    contador += 1
    # print(n1)
    # print(n2)
    print(sequencia)