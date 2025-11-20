pessoas = []
while True:
    nome = input("Nome: ")
    peso = float(input("Peso: "))

    pessoas.append([nome, peso])

    cond = input("Quer continuar? [S/N] ").strip().lower()
    if cond == 'n':
        break

# Descobrir o menor peso
menor_peso = pessoas[0][1]  # peso da primeira pessoa
for p in pessoas:
    if p[1] < menor_peso:
        menor_peso = p[1]

# Mostrar todos que têm esse peso
print(f"\nMenor peso encontrado: {menor_peso} kg")
print("Pessoa(s) com esse peso:")

for p in pessoas:
    if p[1] == menor_peso:
        print(f" - {p[0]}")