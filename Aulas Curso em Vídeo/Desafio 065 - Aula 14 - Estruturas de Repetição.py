print('Calculadora de números aleatórios!!')
cond = ['sim', 'não']
numtotal = 0
contador = 0
numeros = []
while True:
    if cond == cond[0]:
        num = int(input('\nDigite o número que você gostaria de adicionar na sua soma: '))
        cond = str(input('\nVocê gostaria de continuar somando: ')).lower()
        numeros.append(num)
        numtotal = num + numtotal
        contador += 1
    elif cond == cond[1]:
        print('\nVocê escolheu sair!')
        print('\nEncerrando o programa!!!')
        break
print(f'\nSeus números digitados foram: {numeros}')
print(f'\nA média entre seus números é: {numtotal/contador:.2f}')
print(f'\nO maior entre seus números é: {max(numeros)}')
print(f'\nO menor entre seus números é: {min(numeros)}')
print(f'\nO somatório total entre seus números é: {numtotal}')