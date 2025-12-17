print('-' * 60)
nome = ('CADASTRE UMA PESSOA')
print(f'{nome:^60}')
print('-' * 60)

maiores = homens = mulheres = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    
    if idade >= 18:
        maiores += 1

    while sexo not in 'mf':
        sexo = str(input('Sexo [M/F]: ')).lower().strip()[0]

    if sexo == 'm':
        homens += 1

    if sexo in 'f' and idade < 20:
        mulheres += 1

    opção = ' '
    while opção not in 'sn':
        print('-' * 60)
        opção = str(input('Quer Continuar? ')).lower().strip()[0]
        print('-' * 60) 
    
    if opção == 'n':
        break

if homens == 0:
    print('\nNão temos homens cadastrados.') 

elif homens == 1:
    print(f'\nTemos {homens} homem cadastrado.')

else:
    print(f'\nTemos ao todo {homens} homens cadastrados.')

    
if maiores == 0:
    print('\nNão temos maiores cadastrados.')

elif maiores == 1:
    print(f'\nTemos apenas {maiores} pessoa com mais de 18 anos.')

else:
    print(f'\nTotal de pessoas com mais de 18 anos: {maiores}')


if mulheres == 0:
    print('\nNão temos mulheres menores cadastradas.')

elif mulheres == 1:
    print(f'\nTemos apenas {mulheres} mulher com menos de 20 anos.')

else:
    print(f'\nTemos {mulheres} mulheres com menos de 20 anos.')

print()
print()
print()
    