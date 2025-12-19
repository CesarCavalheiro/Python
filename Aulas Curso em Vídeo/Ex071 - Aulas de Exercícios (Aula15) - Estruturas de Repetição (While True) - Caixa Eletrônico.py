print('='*40)
nome = 'BANCO CESAR'
print(f'{nome:^40}')
print('='*40)

saque = int(input('Qual valor você quer sacar? '))

total = saque
nota = 100
contnotas = 0

while True:

    if total >= nota:
        total -= nota
        contnotas += 1

    else:
        if contnotas > 0:
            print(f'Total de {contnotas} notas de R$ {nota}')
            contnotas = 0

        if nota == 100:
            nota = 50

        elif nota == 50:
            nota = 20

        elif nota == 20:
            nota = 10

        elif nota == 10:
            nota = 5

        elif nota == 5:
            nota = 1

        if total == 0:
            break
h