contador = 1
pessoas = 0
maiores = 0  
homens = 0
mulheresmenores = 0
m = ''
f = ''

while True:

    print(f'\nDigite os dados da {contador}ª pessoa: ')
    contador += 1
    nome = str(input('\nNome: '))
    idade = int(input('\nIdade: '))
    sexo = str(input('\nSexo [M/F]: ')).lower()
    
    while sexo not in ('f', 'm'):
        sexo = str(input('\nSexo [M/F]: ')).lower()

    
    if nome != '':
        pessoas += 1

    if idade > 18:
        maiores += 1
        
    
    if sexo == 'm':
        homens += 1
           

    if sexo == 'f' and idade < 20:
        mulheresmenores += 1

    continuar = str(input('\nDeseja continuar? [S/N] '))
        
    while not continuar in ('s', 'n'):
        continuar = str(input('\nDeseja continuar? [S/N] '))

    if continuar == 'n':
        break

print(f'''\nFoi cadastrado um total de {pessoas} pessoas!
      
Dentre elas: 

{maiores} delas são maiores que 18 anos!

{homens} delas são homens!

Um total de {mulheresmenores} pessoas, são mulheres menores que 20 anos!!!''')

print(' ')
print(' ')

    