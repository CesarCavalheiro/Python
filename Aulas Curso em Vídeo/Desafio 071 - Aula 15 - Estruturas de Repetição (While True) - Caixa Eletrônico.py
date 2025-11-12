nome = 'CAIXA ELETRÔNICO'
print('=' * 50)
print(f'{nome:^50}')
print('=' *50)

valor = int(input('Qual o valor que você deseja sacar? '))

cedula50 = valor // 50
cedula20 = (valor % 50) // 20
cedula10 = (valor % 50) % 20 // 10
cedula5 = (((valor % 50) % 20 )% 10) // 5
cedula1 = ((((valor % 50) % 20 )% 10) % 5) // 1

if cedula50 > 0:
    print(f'\nTotal de {cedula50} cédulas de R$ 50,00'.replace('.' , ','))

if cedula20 > 0:
    print(f'\nTotal de {cedula20} cédulas de R$ 20,00'.replace('.' , ','))

if cedula10 > 0:
    print(f'\nTotal de {cedula10} cédulas de R$ 10,00'.replace('.' , ','))

if cedula5 > 0:
    print(f'\nTotal de {cedula5} cédulas de R$ 5,00'.replace('.' , ','))

if cedula1 > 0:
    print(f'\nTotal de {cedula1} cédulas de R$ 1,00'.replace('.' , ','))

print('')
print('')
print('')