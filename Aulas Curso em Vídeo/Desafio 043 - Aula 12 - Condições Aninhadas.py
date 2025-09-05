peso = float(input('Digite seu Peso: '))
altura = float(input('Digiteu sua altura: '))
imc = peso/altura**2
if imc < 18.5:
    print (f'Seu IMC é de {imc:.2f}, você está abaixo do peso ideal!!')
elif 18.5 <= imc < 25:
    print(f'Seu IMC é de {imc:.2f}, você está no seu peso ideial!!')
elif 25 <= imc < 30:
    print(f'Seu IMC é de {imc:.2f}, você está obeso!!')
else:
    print(f'Seu IMC é de {imc:.2f}, seu quadro é de obesidade Mórbida!!')

