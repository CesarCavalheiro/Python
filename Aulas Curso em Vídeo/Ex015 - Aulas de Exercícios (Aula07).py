dias = float(input('Por quantos dias o carro ficou alugado? '))
km = float(input('Quantos km\'s você rodou? '))
print(f'Considerando a quantidade de {dias} diárias mais o quantidade de {km} km\'s rodados, o valor total a pagar é de R${dias*60+km*0.15:.2f}.')