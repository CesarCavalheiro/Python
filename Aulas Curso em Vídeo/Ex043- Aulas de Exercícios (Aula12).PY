print('*** Calculadora de IMC ***')

peso = float(input('\nDigite seu peso: ').replace(',','.'))
altura = float(input('\nDigite sua altura: ').replace(',','.'))
imc = peso / altura**2

if imc < 18.5:
    print(f'\nVocê tem {altura:.2f}m e {peso:.2f} quilos, seu imc é {imc:.2f}, você está abaixo do peso! ')

elif imc < 25:
    print(f'\nVocê tem {altura:.2f}m e {peso:.2f} quilos, seu imc é {imc:.2f}, você está no seu peso ideal! ')

elif imc < 30:
    print(f'\nVocê tem {altura:.2f}m e {peso:.2f} quilos, seu imc é {imc:.2f}, você está com sobrepeso! ')

elif imc < 40:
    print(f'\nVocê tem {altura:.2f}m e {peso:.2f} quilos, seu imc é {imc:.2f}, você está obeso! ')

else:
    print(f'\nVocê tem {altura:.2f}m e {peso:.2f} quilos, seu imc é {imc:.2f}, você está com obesidade mórbida! ')
