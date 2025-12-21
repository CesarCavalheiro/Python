times = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Fluminense', 'Botafogo', 
'Bahia', 'São Paulo', 'Grêmio', 'Bragantino', 'Atlético Mg', 'Santos', 'Corinthians', 
'Vasco da Gama', 'Ec Vitória', 'Internacional', 'Ceara Sc', 'Fortaleza', 'Juventude', 'Sport Recife')

print(f'Os cinco primeiros colocados são: {times[0:5]}')
print(f'Os times que foram rebaixados foram: {times[16:20]}')
print(sorted(times))

posição = int(input('De qual posição você gostaria de ver o time? '))

print(f'Na posição {posição} ficou o {times[posição-1]}')

posição = str(input('De qual time você gostaria de ver a posição? '))

cont = 1
encontrou = False

for t in times:
    if t == posição:
        print(f'{posição} está na posição {cont}')
        encontrou = True
        break
    cont += 1