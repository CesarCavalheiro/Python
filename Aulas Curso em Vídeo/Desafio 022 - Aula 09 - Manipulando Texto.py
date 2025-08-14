# frase = 'Curso em Vídeo Python'
# print(len(frase))
# print(frase.count('o'))
# print(frase.count('o', 0, 13))
# print(frase.find('deo'))
# print(frase.find('Android'))
# print('Curso' in frase)
# print(frase.replace('Python', 'Android'))
# print(frase.upper())
# print(frase.lower())
# print(frase.capitalize())
# print(frase.title())

# # O Len serve para mostrar o tamanho da string em quantidade de caracteres.
# # O Count serve para contar, no caso acima mandamos contar quantos "O's" tem na frase.
# # É possível fazer uma contagem já com fatiamento conforme demonstrado no print 3. No caso mandamos contar quantos "o's" temos entre 0 e 13.
# # É possível também mandar procurar alguma coisa dentro da frase, no print 4 mandamos procurar "deo" dentro da nossa frase. O Python responderá 11 que é onde começa o "deo"
# # No quinto print mandamos procurar uma palavra que não existe na nossa frase, a isso o Python retorna -1, pois essa palavra não existe.
# # No sexto print vemos o funcionamento da função "in". A utilizamos para perguntar existe a palavra "Curso" na nossa frase? Caso sim a resposta será True, caso não, False.
# # Replace - A função replace é utilizada para promover alterações nos nossos textos, no nosso caso mandamos alterar de Python para Android.
# # Upper - Utilizamos o Upper para transformar tudo para maísculo.
# # Lower - Igual ao Upper porém transforma tudo para minúsculo.
# # Capitize e Title. Capitalize vai deixar somente a primeira letra da nossa frase em maiúscula, já o Title vai deixar a primeira letra de cada palavra em maiúsculo.

# frase1 = ('   Aprenda Python  ')
# print(frase1)
# print(frase1.strip())
# print(frase1.lstrip())
# print(frase1.rstrip())

# # Perceba que foram digitados alguns espaços a mais propositalmente, para retirarmos esses espaços usamos o "strip"
# # Podemos usar ainda lstrip para tirarmos apenas os espaços a esquerda ou rstrip para tirarmos apenas os espaços a direita.

# frase2 = (frase.split())
# print(frase2[2])
# print('-'.join(frase2))

# Split - Utilizamos o split para dividirmos a frase, o split dividirá a frase entre todas as suas palavras criando assim uma lista com as palavras da frase.
# Join -  Usamos o Join para "concatenar" o caractere antes do join com a frase após ele.

nome = input('Digiteu seu nome completo: ')
print(nome.upper())
print(nome.lower())
print(nome.replace(' ',''))
print(len(nome.replace(' ','')))
nome2 = ((nome.split()))
print(len(nome2[0]))