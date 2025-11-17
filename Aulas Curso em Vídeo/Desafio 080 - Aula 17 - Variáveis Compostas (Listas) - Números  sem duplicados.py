lista = []

for i in range(0,5):
    valor = (int(input('Digite um valor: ')))
    lista.append(valor)

    print(f'o indice é {i})')
    indiceanterior = i-1
    
    for posição, numero in enumerate(lista):
        print(f'A posição é {posição} e o número é {numero}')

valor = lista[2]
   
print(valor)