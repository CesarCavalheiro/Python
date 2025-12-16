while True:

    n = int(input('Você gostaria de ver a tabuada de qual número? '))

    if n < 0:

        print('\nPrograma Encerrado! Volte sempre que precisar!!!')

        break

    print('-'*40)

    for i in range(0,11):

        print(f'{n} x {i} = {n*i}')

    print('-'*40)

print()
print()
print()
        
    