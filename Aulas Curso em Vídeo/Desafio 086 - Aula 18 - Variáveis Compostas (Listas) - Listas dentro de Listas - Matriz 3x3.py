matriz = []

for numero in range(0,3):
    linha = []
    for numero1 in range(0,3):
        valor = int(input(f'Digite o valor para a posição[{numero}][{numero1}]: '))
        linha.append(valor)
    matriz.append(linha)


for linha in matriz:
    for valor in linha:
        print(f'\n[{valor}]', end='')
    print()
    
