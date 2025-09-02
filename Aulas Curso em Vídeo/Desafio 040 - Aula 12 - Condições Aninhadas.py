nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2)/2
if media < 5.0:
    print(f'Sua média é {media}, você ficou abaixo de 5.0! Status: REPROVADO!')
elif media <= 6.9:
    print(f'Sua média é {media}, você ficou entre 5.0 e 6.9! Status: RECUPERAÇÃO!')
else: 
    print(f'Sua média é {media}, você ficou acima de 6.9! Status: APROVADO!') 


