# Maneira matemática de fazer
# co = float(input('Digite o comprimento do cateto oposto: '))
# ca = float(input('Digite o comprimento do cateto adjacente: '))
# print(f'A hipotenusa vai medir: {((co**2)+(ca**2))**0.5:.2f}')

# Maneira importando a função hypot do módulo de matemática
# from math import hypot
# co = float(input('Digite o comprimento do cateto oposto: '))
# ca = float(input('Digite o comprimento do cateto adjacente: '))
# print(f'Para os seus catetos a hipotenusa é: {hypot(co, ca)}')

#Maneira importando a função Raiz Quadrada do módulo de matemática
from math import sqrt
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
print(f'Para os seus catetos a hipotenusa é {sqrt(ca**2+co**2)}')
