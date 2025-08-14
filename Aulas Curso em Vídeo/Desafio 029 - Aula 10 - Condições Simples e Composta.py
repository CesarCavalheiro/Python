velocidade = int(input('Digite a velocidade do veículo: '))
ultrapassado = velocidade - 80
if velocidade > 80:
    print(f"""Você estava a {velocidade}Km/h. Você ultrapassou o limite de 80km em {ultrapassado}Km.
A multa nesse caso é de R$ 7,00 para cada km acima da máxima. Sua multa é: R${ultrapassado * 7:.2f}""")

