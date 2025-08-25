km = float(input('Digite a distância da sua viagem: '))
print (f'Sua viagem será de {km:.2f} Km.')
if(km<=200):
    print(f'Sua viagem ficaré em R$ {km*0.50:.2f}.')
else:
    print(f'Sua viagem ficará em R$ {km*0.45:.2f}.')