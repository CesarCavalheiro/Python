cont = soma = maior = menor = 0
opção = 's'

while opção in 'Ss':

    n = int(input('\nDigite um número para somá-lo: '))

    opção = str(input('\nDeseja continuar [S/N]: ')).strip()[0]

    cont += 1

    soma += n


    if cont == 1:

        maior = menor = n

    else:
        if n > maior:
            maior = n

        else:
            if n < menor:
                menor = n

print(f'\nVocê digitou {cont} numeros e a media entre eles foi de {soma/cont}')

print(f'\nO maior valor digitado foi {maior} e o menor foi {menor}')

print()
print()
print()