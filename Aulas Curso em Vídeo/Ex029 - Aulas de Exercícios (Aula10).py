velocidade = float(input('Qual é a velocidade atual do carro?\033[1;32m '))
if(velocidade <= 80):
    print('Dirija com segurança!')
else:
    print(f'\033[1;31mMULTADO! Você execedeu o limite de velocidade em {velocidade-80:.2f}Km/h.\033[m \nSua multa será de R$ {(velocidade-80)*7:.2f}! Dirija com segurança e RESPEITE OS LIMITES DE VELOCIDADE.')
print('\033[33mTenha um bom dia!!!\033[m')