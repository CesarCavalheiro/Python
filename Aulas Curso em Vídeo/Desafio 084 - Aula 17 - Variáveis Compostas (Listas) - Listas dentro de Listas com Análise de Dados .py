lista = []
menor_peso = ''


cont = 0
condição = 's'

while True:
    if condição == 's':
    
        cont += 1

        nome = str(input(f'\nNome: '))

        peso = float(input('\nPeso: '))

        lista.append([nome, peso])

        condição = str(input('\nQuer continuar [S/N]: ' ).lower())

    menor_peso == lista[0][1]

    for pessoas in lista:
        if pessoas[1] < menor_peso:
            menor_peso = pessoas[1]

    print(f'\nMenor peso encontrado foi: {peso} Kg!')

    for pessoas in lista:
        if p[1] == menor_peso:
            print(f'\n - {p[0]}')

       

        condição = str(input('\nQuer continuar [S/N]: ' ).lower())

        

            
           
    else:

        print('\nVocê escolheu sair!!!')
        break

print(f'Ao todo, você cadastrou {cont} pessoas.') 
 
