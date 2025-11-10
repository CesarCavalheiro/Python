while True:
    n = int(input('\nDigite o número desejado para saber qual é a sua tabuada: '))
    print('-' * 60)
    if n < 0:
        break
    for t in range (1,11):
        print(f'{n} x {t:2} = {n*t}')
    print('-' * 60)
     