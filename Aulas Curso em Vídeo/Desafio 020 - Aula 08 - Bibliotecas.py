from random import shuffle
alunos = input('Digite o nome dos seus alunos: ')
lista = alunos.split()
shuffle(lista)
print('A ordem de apresentação dos seus alunos será: ', ', '.join(lista))