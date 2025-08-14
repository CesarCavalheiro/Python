palavra = input('Digite uma palavra qualquer: ').upper()
print(f"""Sua palavra é: {palavra}, sua palavra tem {palavra.count('A')} letras \"A\'s\". 
Sua primeira letra \"A\" aparece na posição {palavra.find('A')}
A última vez que a letra \"A\" aparece é na posição {palavra.rfind('A')} """)
