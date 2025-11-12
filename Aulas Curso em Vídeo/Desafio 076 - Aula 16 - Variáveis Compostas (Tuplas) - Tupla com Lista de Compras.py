print()
print()
print()

nome = ('LISTAGEM DE PREÇOS')
print('-'*60)
print(f'{nome:^60}')
print('-'*60)

listagem = ('Lapis', '1,75', 
            'Borracha', '2,00',
            'Caderno', '15,90',
            'Estojo', '25,00',
            'Transferidor', '4,20',
            'Compasso', '9,99',
            'Mochila', '120,32',
            'Canetas', '22,30',
            'Livro', '34,90',
            )

for i in range(0, len(listagem), 2):
    produto = listagem[i]
    preço = listagem[i+1]

    print(f'{produto:.<50}R$ {preço:>6}')
   

print('-'*60)
            



print()
print()
print()