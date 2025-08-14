#Vamos fazer um programa que leia os catetos oposto e adjacente e calcule a hipotenusa. Faremos isso matemáticamente e posteriormente com módulos.

# ca = float(input('Digite seu cateto adjacente: '))
# co = float(input('Digite seu cateto oposto: '))
# print(f'Seu cateto adjacente é: {ca}, seu cateto oposto é: {co}, sua hipotenusa é: {(ca**2+co**2)**0.5}')

#Agora vamos ver como isso ficaria com módulos.

# from math import hypot

# ca = float(input('Digite seu cateto adjacente: '))
# co = float(input('Digite seu cateto oposto: '))
# print(f'Seu cateto adjacente é: {ca}, seu cateto oposto é: {co}, sua hipotenusa é: {hypot(ca, co)}')

#Outra forma ainda de fazer com módulos

from math import sqrt
ca = float(input('Digite seu cateto adjacente: '))
co = float(input('Digite seu cateto oposto: '))
print(f'Seu cateto adjacente é: {ca}, seu cateto oposto é: {co}, sua hipotenusa é: {sqrt(ca**2+co**2)}')