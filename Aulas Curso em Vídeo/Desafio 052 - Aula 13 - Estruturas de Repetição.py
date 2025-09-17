numero = int(input('Digite seu número: '))
if numero > 1:
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
    if primo: 
        print(f'{numero} é Primo!!')
    else:
        print(f'{numero} não é primo!!')    
else: 
    print('Números menores ou iguais a 1 não são primos')





