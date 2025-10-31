print('Calculadora de números aleatórios!!')
cond = 'sim'
numtotal = 0
contador = 0
numeros = []

while True:
    if cond == 'sim':
        num = int(input('\nDigite o número que você gostaria de adicionar na sua soma: '))
        cond = input('\nVocê gostaria de continuar somando? (Digite apenas sim ou não): ').lower()
        numeros.append(num)
        numtotal = num + numtotal
        contador += 1

        while cond != 'sim' and cond != 'não':
            print('\nOpção inválida! Você precisa digitar "Sim" ou "Não".')
            cond = input('\nTente novamente com sim ou não: ')
    else:
        print('\nVocê escolheu sair!')
        print('\nEncerrando o programa!!!')
        break

print(f'\nSeus números digitados foram: {numeros}')
print(f'\nA média entre seus números é: {numtotal/contador:.2f}')
print(f'\nO maior entre seus números é: {max(numeros)}')
print(f'\nO menor entre seus números é: {min(numeros)}')
print(f'\nO somatório dos seus número é: {numtotal}')