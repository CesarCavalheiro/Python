lista = []
listanotas = []
cont = 0
pergunta = ('s')

while pergunta == 's':

    cont += 1
    nome = str(input(f'\nNome do {cont}º aluno: '))
    nota1 = float(input('\n1ª Nota: ').replace(',' , '.'))
    nota2 = float(input('\n2ª Nota: ').replace(',' , '.'))
    média = (nota1 + nota2) / 2
    
    lista.append([nome, [nota1, nota2],média])

    pergunta = str(input('\nQuer continuar? [S/N]: ').lower())


print('-='*20)
print(f'{'\nNº':<6}{"NOME":<20}{"MÉDIA":>10}')
print('='*40)
    
for i, pessoa in enumerate(lista, start=1):
    nome = pessoa[0]
    media = pessoa[2]
    listanotas.append((f'{i:<5}{nome:<20}{(media):>10.1f}'))

for linha in listanotas:
    print(linha)
print('='*40)

while True:

    aluno = int(input('Mostrar nota de qual aluno? (999 interrompe): '))

    if aluno == 999:
        break
    
    if aluno < 1 or aluno > len(lista):
        print('Aluno Inexistente')
        continue

    notas = lista[aluno -1][1]
    print(f'As notas de {nome} são {notas} ')