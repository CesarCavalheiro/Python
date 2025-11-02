print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
primeiro = float(input('\nPrimeiro Segmento: '))
segundo = float(input('\nSegundo Segmento: '))
terceiro = float(input('\nTerceiro Segmento: '))
if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < primeiro + segundo:
    print('\nSeus segmentos formam um triângulo!!')
    
    if primeiro == segundo == terceiro:
        print('\nSeu triângulo tem todos os lados iguas e portanto é um EQUILÁTERO!')
    
    elif primeiro != segundo != terceiro != primeiro:
        print('\nSeu triângulo tem todos os lados diferentes e portanto, é um ESCALENO!')

    else:
        print ('\nSeu triângulo tem um lado diferente e portanto é ISÓCELES!')

else:
    print('\nSeu segmentos não formam um triângulo!!')