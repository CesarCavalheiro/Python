nomes = []
idades = []
sexos = []

menoridade = 0
sexof = 0
anciao = ''
ancião = ''

for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()

    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)

    if sexo == 'F':
        sexof += 1

    if sexo == 'F' and idade < 20:
        menoridade += 1

    if sexo == 'M' and idade == max(idades):
        anciao = idade
        ancião = nome


print(f'\nA média de idade do grupo é {sum(idades)/4:.2f} anos!')

if sexof < 3:
    print(f'\nO homem mais velho do grupo tem {anciao} anos e seu nome é {ancião}!')

if sexof == 0:
    print('\nNão há mulheres no grupo!')

if sexof > 0 and menoridade == 0:
    print('\nNão há mulheres com menos de 20 anos no grupo!')
    
if sexof >= 1 and menoridade == 1:
   print(f'\nHá uma mulher com menos de 20 anos no grupo!')

if sexof >= 1 and menoridade >= 2:
    print(f'\nAo todo são {menoridade} mulheres com menos de 20 anos no grupo!')

