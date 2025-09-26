print('Digite o peso de 5 Pessoas, depois diga qual é o maior e o menor peso\n')

pesos = []

for c in range(1,6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
    pesos.append(peso)

print(max(pesos))
print(min(pesos))
