numero = int(input('Digite seu número: '))
print(f"""Seu número é {numero}
Seu número tem: 
{numero // 1000 % 10} milhar(es)
{numero // 100 % 10} centena(s)
{numero // 10 % 10} dezena(s)
{numero // 1 % 10} unidade(s)""")

#Matemáticamente o módulo "%" resto literalmente calcula e mostra apenas o resto do cálculo exemplo: 4576 / 1000 = 4,576 esse resultado ao dividor por 10 que é o valor do módulo da 0,4576 logo é esse o resultado mostrado.