num = int(input('Digite seu número: '))

for c in range(1, num, + 1):
    if num % c == 0:
        print('\033[034m', end= '')
    else:
        print ('\033[m', end='')
    print(f'{c} ', end='')