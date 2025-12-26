lista = []

for n in range(0,5):
    numero = int(input('Digite um valor: '))
    if n == 0:
        lista.insert(0, numero)

        
    
    for pos, num in enumerate(lista):
 
        if numero < num:
            lista.insert(n - 
                         1 , numero)

        else: 
            lista.insert(n + 1, numero)
    
    print(lista)
                