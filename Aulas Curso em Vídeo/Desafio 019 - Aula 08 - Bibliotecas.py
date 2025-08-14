import random
alunos = input('Digite os nomes dos seus alunos ')
lista_nomes = alunos.split()
print(f'O aluno sorteado foi: {(random.choice(lista_nomes))}')
