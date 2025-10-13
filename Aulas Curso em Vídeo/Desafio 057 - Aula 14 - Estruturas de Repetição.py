s = ''
while s not in ('M', 'F'):
    s = str(input('Digite seu sexo. Utilize M para Masculino e F para Feminino: ')).upper().strip()
    if s == 'M':
        print('Você é homem')
    if s == 'F':
        print('Você é mulher')
    else:
        print('Comando inválido! Digite apenas M ou F.\n')


