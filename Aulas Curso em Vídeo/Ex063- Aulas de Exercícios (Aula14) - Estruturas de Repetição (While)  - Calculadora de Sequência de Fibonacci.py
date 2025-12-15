print('-'*30)
print('SEQUENCIA DE FIBONACCI')
print('-'*30)


n0 = 1
n1 = 1

termos = int(input(f'Quantos termos você quer mostrar? '))



while termos > 0:

    fibo = n0 + n1


    termos -= 1

    print(fibo)

