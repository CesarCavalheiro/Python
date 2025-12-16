reset = '\033[0m'

# Cores básicas
preto = '\033[30m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
magenta = '\033[35m'
ciano = '\033[36m'
branco = '\033[37m'

from datetime import date
anoatual = date.today().year

contador = 0
maiores = 0

for i in range(0 , 7):
    contador += 1
    idade = int(input(f'Digite o ano de nascimento da {contador}ª pessoa: {verde}'))
    print(reset)
    if anoatual - idade > 18:
        maiores += 1
print(f'Ao todo tivemos {maiores} pessoas maiores de idade e também {contador - maiores} pessoas menores de idade')