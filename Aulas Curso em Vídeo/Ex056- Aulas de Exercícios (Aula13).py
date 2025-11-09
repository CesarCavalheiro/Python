nomes = []
idades = []
sexos = []

menoridade = 0


for p in range(1, 4):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()

    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)

    if sexo == 'F' and idade < 20:
        menoridade += 1
    
#print(f'\nA média de idade do grupo é {sum(idades)/3}')
    
    if sexo == 'M' and idade == max(idades):
        print(f'\nO homem mais velho do grupo tem {idade} e seu nome é {nome}!')

#     else:
#         print('\nNão há homens no grupo!')

# if menoridade == 0:
#     print('\nNão há mulheres com menos de 20 anos no grupo!')
    
# elif menoridade < 2:
       
#     print(f'\nHá uma mulher com menos de 20 anos no grupo!')

# else:
        
#     print(f'\nAo todo são {menoridade} mulheres com menos de 20 anos no grupo!')

    

