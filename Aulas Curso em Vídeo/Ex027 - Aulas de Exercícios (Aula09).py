nome = input('Digite seu nome completo: ').strip()
nomedividido = (nome.split())
print(f"""Olá {nomedividido[0]}, prazer em te conhecer
Seu primeiro nome é: {nomedividido[0]} 
Seu último nome é: {nomedividido[-1]}""")