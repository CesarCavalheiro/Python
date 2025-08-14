from random import choice
alunos = input('Digite o nome dos aluno: ')
lista_alunos = alunos.split()
print(f'O aluno escolhido foi {choice(lista_alunos)}')
