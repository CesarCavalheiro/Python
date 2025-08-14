#São operadores aritiméticos em Python
# + Adição
# - Subtração
# * Multiplicação
# / Divisão 
# ** Potência
# // Divisão Inteira
# % Resto da Divisão

# Obs.: Quando em Python preciso usar um símbolo de igual, vou usar então dois símbolos pois um só serve como atribuidor a uma variável. Exemplo ==

# Quando trabalhamos com operadores aritiméticos o Python assim como a matemática normal tem uma ordem de precedência que é a seguinte:
# Primeiro o que estiver entre parênteses
# Segundo as potências
# Terceiro Multiplicação, Divisão, Divisão Inteira e Resto da Divisão, respeitando a ordem da esquerda para a direita
# Quarto Adição e Subtração

numero = int(input('Digite seu número: '))
print(f'Seu número é: {numero}, seu antecessor é: {numero-1} e seu sucessor é: {numero+1}')