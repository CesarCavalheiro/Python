expressão = str(input('Digite sua expressão: '))
pilha = []

for caracter in expressão:

    if caracter == '(':
        pilha.append('(')

    elif caracter == ')':
        if len(pilha) > 0:
            pilha.pop()

        else:
            pilha.append(')')
            break

if len(pilha) == 0:
        
    print('Sua expressão é válida')

else:
    print('Sua expressão é inválida. Há parênteses abertos.')