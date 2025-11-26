pessoas = []

cont = 0

while True:
    nome = input('\nNome: ')
    peso = float(input('\nPeso: '))

    pessoas.append([nome, peso])
    cont += 1

    maior = max(p[1] for p in pessoas)
    menor = min(p[1] for p in pessoas)

    maiorpessoa = [p[0] for p in pessoas if p[1] == maior]
    menorpessoa = [p[0] for p in pessoas if p[1] == menor]
   

    cond = input('\nQuer continuar? [S/N] ').strip().lower()
    if cond == 'n':
        break

print(f'\nForam cadastradas um total de {cont} pessoas')

print(f'\nO Maior peso foi de {maior}Kg. Peso de {maiorpessoa}')

print(f'\nO Menor peso foi de {menor}Kg. Peso de {menorpessoa}')