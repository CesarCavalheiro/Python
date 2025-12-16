print('Calculadora de notas')
n1 = float(input('\nDigite a primeira nota do aluno: ').replace(',','.'))
n2 = float(input('\nDigite a segunda nota do aluno: ').replace(',','.'))
media = (n1 + n2)/2
print(f'\nSua primeira nota foi {n1}, sua segunda nota foi {n2}, sua média é {media:.2f}.')

if media < 5:
    print(f'\nSua média ficou em {media}, você não alcançou a média proposta em {media - 7:.2f} ponto(s) e portanto está em REPROVADO.')
    print(f'\nVocê ficou a {media-5:.2f} pontos de poder fazer a recuperação!')

elif 7 > media >= 5:
    print(f'\nSua média ficou em {media}, sua nota não foi suficiente para passar direto, porém você poderá fazer a RECUPERAÇÃO.')

else:
   print(f'\nSua média ficou em {media}, você ultrapassou a média proposta em {media - 7:.2f} ponto(s) e portanto está APROVADO!!')