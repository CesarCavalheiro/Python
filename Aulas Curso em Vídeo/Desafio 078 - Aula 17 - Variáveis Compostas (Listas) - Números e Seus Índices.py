lista = []

for i in range(0,5):
    lista.append(int(input(f'\nDigite um valor para a Posição {i}: ')))

print(f'\nVocê digitou os valores: {lista}')

maior = max(lista)
menor = min(lista)
posiçãomaior = [posição for posição, valor in enumerate(lista) if valor == maior]
posiçãomenor = [posição for posição, valor in enumerate(lista) if valor == menor]


if len(posiçãomaior) == 1:
    print(f'\nO maior valor digitado foi {maior} na posição {posiçãomaior}')

else: print(f'\nO maior valor digitado foi {maior} nas posições {posiçãomaior}')

        
if len(posiçãomenor) == 1:
    print(f'\nO menor valor digitado foi {menor} na posição {posiçãomenor}')

else: print(f'\nO menor valor digitado foi {menor} nas posições {posiçãomenor}')

 
    
print( )
print( )

