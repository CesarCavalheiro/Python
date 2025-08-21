distancia = float(input('Qual será a distância da sua viagem? '))
if distancia <=200:
    print(f'Sua passagem custará R$ {distancia*0.5}')
else:
    print(f'Sua passagem custará R$ {distancia*0.45}')