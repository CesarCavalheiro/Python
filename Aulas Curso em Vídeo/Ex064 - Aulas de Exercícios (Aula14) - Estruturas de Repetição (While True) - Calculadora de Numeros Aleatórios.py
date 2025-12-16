n = ntotal = cont = 0

n = int(input('\nDigite um número para somá-lo [Digite 999 para parar]: '))

while n != 999:

    ntotal += n

    cont += 1

    n = int(input('\nDigite um número para somá-lo [Digite 999 para parar]: '))

print(f'\nVocê digitou {cont} números para serem somados e a soma total entre eles é: {ntotal}')

print()
print()
print()

    
