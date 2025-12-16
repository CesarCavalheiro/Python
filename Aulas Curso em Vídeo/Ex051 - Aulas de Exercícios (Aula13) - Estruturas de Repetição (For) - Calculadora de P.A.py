print('=' * 40)
print('          10 TERMOS DE UMA PA')
print('=' * 40)
termo = int(input('\nDigite seu primeiro termo: '))
razao = int(input('Digite a razão: '))
pa = termo + (10 - 1) * razao
for t in range(termo, pa, razao):
    print(t, end=' --> ') 
print('ACABOU')


