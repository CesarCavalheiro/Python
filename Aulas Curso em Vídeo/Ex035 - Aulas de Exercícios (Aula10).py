print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
primeiro = float(input('Primeiro Segmento: '))
segundo = float(input('Segundo Segmento: '))
terceiro = float(input('Terceiro Segmento: '))
if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < primeiro + segundo:
    print('Seus segmentos formam um triângulo!!')
else:
    print('Seu segmentos não formam um triângulo!!')