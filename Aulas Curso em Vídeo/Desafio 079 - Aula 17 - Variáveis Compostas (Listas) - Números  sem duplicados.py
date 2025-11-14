lista = []
condição = ()

while True:
    
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('\nValor duplicado! Não será adicionado!!!')
    else:
        print('\nValor adicionado com sucesso!!!')
        lista.append(valor)
    
    condição = str(input('\nQuer continuar? [S/N] ').lower())

    if condição == 's':
        print()
    else: 
        print('\nSaindo do programa!!!')

        break        

lista.sort()

print(f'\nVocê digitou os valores únicos {lista}.')
    
