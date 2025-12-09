matriz = []
total = 0

for numero in range(0,3):
    linha = []
    for numero1 in range(0,3):
        valor = int(input(f'Digite o valor para a posição[{numero}][{numero1}]: '))
        linha.append(valor)
    
    matriz.append(linha)

print('-=' * 20)
for linha in matriz:
    
    for valor in linha:
        
        if valor % 2 == 0:
            total = valor + total

        print(f'[{valor}]', end='')
    print()
    
    
print('-=' *20)

print(f'A soma dos valores pares é {total}')
print(f'A soma dos valores da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'O maior valor da segunda linha é {max(matriz[1][0], matriz[1][1] ,matriz[1][2])}')