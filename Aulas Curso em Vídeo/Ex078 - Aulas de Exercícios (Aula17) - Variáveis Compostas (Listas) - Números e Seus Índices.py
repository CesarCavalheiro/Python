lista = []

for pos in range(0,5):
    lista.append(int(input(f'\nDigite um valor para a posição {pos}: ')))
    
print(f'\nVocê digitou os valores {lista}')

maior = menor = 0 

for valor in lista:
    if valor > maior:
        maior = valor

for valor in lista:
    if valor < menor:
        menor = valor

print(maior)
print(menor)