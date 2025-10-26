print('Calculadora de Números Aleatórios')
contador = 0
while True:
    if n != 999:
        n = int(input('Digite seu número: '))
        n1 = n
        n2 = n1 + n
        contador += 1
        print(n2)
    else:
        print('Encerrando o programa!')
        break