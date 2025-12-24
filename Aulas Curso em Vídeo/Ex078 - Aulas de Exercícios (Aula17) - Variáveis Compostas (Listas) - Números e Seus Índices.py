lista = []
maior = menor = 0

for pos in range(0,5):
    lista.append(int(input(f'\nDigite um valor para a posição {pos}: ')))
    if pos == 0:
        maior = menor = lista[pos]
 
    else:
        if lista[pos] > maior:
            maior = lista[pos]
        if lista[pos] < menor:
            menor = lista[pos]
   
print('=-' * 30)
    
print(f'Você digitou os valores {lista}')

print(f'O maior valor digitado foi {maior} nas posições ' , end='')

for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...' , end=' ')

print(f'\nO menor valor digitado foi {menor} nas posições ' , end='')

for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...' , end=' ')



