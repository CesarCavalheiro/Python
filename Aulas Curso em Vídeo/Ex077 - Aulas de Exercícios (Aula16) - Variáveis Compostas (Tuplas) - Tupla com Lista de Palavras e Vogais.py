palavras = ('Aprender', 'Programar', 'Linguagem', 'Python',
'Curso', 'Gratis', 'Estudar', 'Pratica', 'Trabalhar', 'Mercado',
'Programador', 'Futuro')

vogais = ''

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogais:', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

    
