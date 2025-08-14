nome = str(input('Digite seu nome completo: '))
nome_dividido = (nome.split())
nome_sem_espaços = (nome.replace(' ',''))
print('Analisando o seu nome...')
print(f"""Com todos os caracteres maiúsculos fica: {nome.upper()}
Com todos os caracteres em minúsculo fica: {nome.lower()}
Seu nome ao todo tem {len(nome_sem_espaços)} letras
Seu primeiro nome é {nome_dividido[0]}
Seu primeiro nome é {nome_dividido[0]} e tem {len(nome_dividido[0])} letras.""")
