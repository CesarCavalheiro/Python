print('Calculadora de números aleatórios!!')
cond = 'SIM'
numtotal = 0
contador = 0
numeros = []
while True:
    if cond == 'SIM':
        num = int(input('\nDigite o número que você gostaria de adicionar na sua soma: '))
        cond = str(input('\nVocê gostaria de continuar somando: ')).upper()
        numeros.append(num)
        numtotal = num + numtotal
        contador += 1
    elif cond != 'SIM' or 'NÃO':
        print('\nVocê digitou um comando inválido, a condição aceita para essa questão é somente Sim ou Não!')
        num = int(input('\nDigite o número que você gostaria de adicionar na sua soma: '))
        cond = str(input('\nVocê gostaria de continuar somando: ')).upper()
        numeros.append(num)
        numtotal = num + numtotal
        contador += 1
        break
    else:
        print('\nVocê escolheu sair!')
        print('\nEncerrando o programa!!!')
        break
print(f'\nSeus números digitados foram: {numeros}')
print(f'\nA média entre seus números é: {numtotal/contador:.2f}')
print(f'\nO maior entre seus números é: {max(numeros)}')
print(f'\nO menor entre seus números é: {min(numeros)}')
print(f'\nO somatório total entre seus números é: {numtotal}')