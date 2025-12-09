from random import randint
from time import sleep

cont = 0

print('-' * 60)
nome = ('SIMULADOR DE JOGOS DA MEGA SENA')
print(f'{nome:^60}')
print('-' * 60)

pergunta = 'Quantos jogos você quer que eu simule?'
largura = 60
texto = f'{pergunta:^{largura}}'
texto = texto.rstrip()
numjogos = int(input(texto + ' '))


print('-=' * 30)
frase = (f'SORTEANDO {numjogos} JOGOS')
print(f'{frase:^60}')
print('-=' * 30)

for j in range(0,numjogos):
    cont += 1

    lista = []
    while len(lista) != 6:
        jogos = randint(1,60)
        if jogos in lista:
            jogos = 'a'
        
        else:   
            lista.append(jogos)
            lista.sort()
    jogo = f'Jogo {cont}: {lista}'
    print(f'{jogo:^60}')
    sleep(1/2)


print('-=' * 11 + '< BOA SORTE!!! >'+ '-=' * 11)
print()
print()
print()




