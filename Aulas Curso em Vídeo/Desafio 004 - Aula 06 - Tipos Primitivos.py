# Em Python temos diversos números primitivos sendo os mais utilizados:
# int = Inteiros. Exemplo de números inteiros: 7, -4, 0, 9875
# Float = Números não inteiros. Exemplo de números não inteiros: 4.5, 0.076, -1.75, 7.0
# Boll = Valor Lógico. Os valores Boleanos só podem ser True ou False
# Str = Strings serão quaisquer valores que aparecerem entre ' ' sendo possível inclusive uma String Vazia.

variavel = input('Digite algo: ')
print(f'O que você digitou é Alpha Numérico? {variavel.isalnum()}')
print(f'O que você digitou é Alphabético? {variavel.isalpha()}')
print(f'O que você digitou é Decimal? {variavel.isdecimal()}')
print(f'O que você digitou está em minúsculo? {variavel.islower()}')
print(f'O que você digitou é está em maiúsculo? {variavel.isupper()}')
print(f'O que você digitou é um espaço? {variavel.isspace()}')
