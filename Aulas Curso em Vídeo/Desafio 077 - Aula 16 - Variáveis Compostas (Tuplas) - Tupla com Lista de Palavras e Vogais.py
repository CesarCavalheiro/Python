palavras = 'APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO'

letra = ''

for words in palavras:
    print(f'\nNa palavra {words} temos: ',end=' ')
    for letra in words:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')