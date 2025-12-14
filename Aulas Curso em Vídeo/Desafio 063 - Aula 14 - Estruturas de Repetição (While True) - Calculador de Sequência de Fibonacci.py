print('Calculadora de Fibonacci')

fibo = int(input('\nDigite a quantidade de número na sequência de Fibonacci que você quer ver: '))
n1 , n2 = 0, 1
contador = 2
print(n1)
print(n2)
while fibo > contador:
    sequencia = n1 + n2
    n1 = n2
    n2 = sequencia
    contador += 1
    print(sequencia)
