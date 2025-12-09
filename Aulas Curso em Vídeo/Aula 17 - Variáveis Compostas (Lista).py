lista = []
listanotas = []
cont = 0
pergunta = 's'

while pergunta == 's':

    cont += 1
    nome = str(input(f'\nNome do {cont}º aluno: '))
    nota1 = float(input('\n1ª Nota: ').replace(',' , '.'))
    nota2 = float(input('\n2ª Nota: ').replace(',' , '.'))
    media = (nota1 + nota2) / 2
    
    lista.append([nome, [nota1, nota2], media])

    pergunta = str(input('\nQuer continuar? [S/N]: ').lower())


print('-='*20)
print(f'{"Nº":<6}{"NOME":<20}{"MÉDIA":>10}')