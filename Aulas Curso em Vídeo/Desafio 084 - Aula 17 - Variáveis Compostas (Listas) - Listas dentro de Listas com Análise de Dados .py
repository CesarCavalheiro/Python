lista = [ ]
cond = 's'
cont = 0
menor_peso = 0

while True:

    if cond == 'S'.lower():
        nome = str(input('\nNome: '))
        peso = float(input('\nPeso: '))
        lista.append([nome, peso])
        

        for pessoa in lista:
            if menor_peso <= peso:
                print(pessoa)
        

        
        
        cond = str(input('\nDeseja continuar? [S/N]: '))

        

    else:
        print('\nVocê escolheu sair!!!')
        break