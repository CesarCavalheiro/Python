print('Digite os nomes, idades e sexo de 4 pessoas.\n')

nomes = []
sexos = []
idades = []

for c in range(1,5):
    nome = input(f'Digite o nome da {c}ª pessoa: ')
    sexo = input(f'Digite o sexo da {c}ª pessoa: ')
    idade = int(input(f'Digite a idade da {c}ª pessoa: '))
    nomes.append(nome)
    sexos.append(sexo)
    idades.append(idade)
soma = sum(idades)/4
print(f'\nQual a idade média do grupo? {soma:.0f} anos!')
