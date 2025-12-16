reset = '\033[0m'
verde = '\033[32m'

lista = []

for i in range(1, 6):
    peso = float(input(f'Digite o peso da {i}ª pessoa {verde}').replace(',' , '.'))
    print(reset)
    lista.append(peso)
print(f'A pessoa com o maior peso pesava, {max(lista)}Kg'.replace('.' , ','))
print(f'A pessoa com menor peso pesava, {min(lista)}Kg'.replace('.' , ','))