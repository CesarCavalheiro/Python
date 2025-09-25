from datetime import datetime
ano_atual = datetime.now().year
maiores = 0
menores = 0
for c in range (1,8):
        nasc = int(input(f'Digite o ano de Nascimento da {c}ª Pessoa: '))
        idade = ano_atual - nasc

        if idade >= 18:
                maiores +=1
        else:
                menores +=1
print(f'\nTotal de maiores de idade:{maiores}')
print(f'Total de menores de idade:{menores}')

                        
   
   
  