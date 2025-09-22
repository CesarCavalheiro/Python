frase = input('Digite a sua Frase: ')
frase = frase.replace(' ','').lower()
invertida = frase[::-1]
if frase == invertida:
   print('Sua frase é um palíndromo!!')
else:
   print('Sua frase não é um palíndromo!!')



