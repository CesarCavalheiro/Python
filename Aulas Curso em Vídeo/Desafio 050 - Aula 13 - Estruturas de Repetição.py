#Há duas possibilidades de fazermos a mesma coisa

# soma = 0
# for numero in range(0,6):
#     if numero % 2 == 0:
#         soma += numero
# print(f'A soma dos pares é: {soma}')

# ou assim mais simplificado

soma = sum(numero for numero in range(0,7) if numero % 2 == 0)
print(f'A soma dos pares é: {soma}')