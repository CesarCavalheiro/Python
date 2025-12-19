print('='*40)
nome = 'BANCO CESAR'
print(f'{nome:^40}')
print('='*40)

saque = int(input('Qual valor você quer sacar? '))

#notas de 100

notas100 = saque // 100

if notas100 == 1:

    print(f'Total de {notas100} nota de R$ 100,00')

else:
    
        print(f'Total de {notas100} notas de R$ 100,00')

resto = saque % 100

#notas de 50

notas50 = resto // 50

resto = resto % 50

if notas50 == 1:

    print(f'Total de {notas50} nota de R$ 50,00')

else:
    
    print(f'Total de {notas50} notas de R$ 50,00')

#notas de 20

notas20 = resto // 20

resto = resto % 20

if notas20 == 1:

    print(f'Total de {notas20} nota de R$ 20,00')

else:
    
    print(f'Total de {notas20} notas de R$ 20,00')

#notas de 10

notas10 = resto // 10

resto = resto % 10

if notas10 == 1:

    print(f'Total de {notas10} nota de R$ 10,00')

else:
    
    print(f'Total de {notas10} notas de R$ 10,00')

#notas de 5

notas5 = resto // 5

resto = resto % 5

if notas5 == 1:

    print(f'Total de {notas5} nota de R$ 5,00')

else:
    
    print(f'Total de {notas5} notas de R$ 5,00')

#notas de 1

notas1 = resto // 1

if notas1 == 1:

    print(f'Total de {notas1} nota de R$ 1,00')

else:
    
    print(f'Total de {notas1} notas de R$ 1,00')


print('\nSaque concluído, volte sempre ao BANCO CESAR')
print('\nTENHA UM BOM DIA!!!')