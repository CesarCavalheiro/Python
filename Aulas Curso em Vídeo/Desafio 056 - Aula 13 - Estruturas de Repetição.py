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
mais_velho = max(idades)
mais_novo = min(idades)
indice_mais_velho = idades.index(mais_velho)
indice_mais_novo = idades.index(mais_novo)
print(f'\nQual a idade média do grupo? {soma:.0f} anos!')
print(f'A pessoa mais velha é {nomes[indice_mais_velho]}, com {mais_velho} anos.')
print(f'A pessoa mais nova é {nomes[indice_mais_novo]} com {mais_novo} anos.')
mulheres_menos_de_20 = 0
for i in range(len(sexos)):
    if sexos[i].upper()== 'F' and idades[i] <20:
        mulheres_menos_de_20 += 1
print(f'A quantidade de mulheres com menos de 20 anos é: {mulheres_menos_de_20}')
