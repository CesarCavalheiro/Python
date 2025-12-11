while True:

    sexo = str(input('\nInforme seu sexo: [M/F] ').lower())
        
    if sexo != 'm' or 'f':
        print('\nDados Inválidos. Por favor, informe seu sexo com M ou F: ')

    else:
        print(f'\nSexo {sexo} registrado com sucesso!')
        break
        
        