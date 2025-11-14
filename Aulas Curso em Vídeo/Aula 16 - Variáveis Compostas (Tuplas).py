
# Obs.: Tuplas são imutáveis

# Uma tupla nada mais é do que uma variável composta conforme podemos ver abaixo:

# As tuplas são compostas de índices que começam com o 0 e vão até o número que se desejar.

# Abaixo temos um exemplo de uma tupla com os índices 0 = 'hamburguer' 1 = 'Suco' 2 = 'Bolo' 3 'Pudim'

lanche = 'Hamburguer', 'Suco', 'Bolo', 'Pudim'

# É possível imprimir a tupla inteira através do comando:

print(lanche) # com a saída ('hamburguer', 'Suco', 'Bolo', 'Pudim')

#ou apenas alguns índices com fatiamento como: 

print(lanche[2]) # com a saída Bolo

# outros exemplos de fatiamento

print(lanche[0:2]) # com a saída ('hamburguer', 'Suco') Aqui o fatiamento imprime os índices 0 e 1 lembrando que no fatiamento o último índice não é considerado

print(lanche[1:]) # com a saída ('Suco', 'Bolo', 'Pudim') Neste caso o fatiamento está pedindo que a impressão pule o índice zero ou seja, que comece no índice 1 e vá até o final pois não há indicação de fim

print(lanche[-1]) # com a saída Pudim Neste caso a impressão acontece de traz para frente começando pelo -1. Caso seja digitado um valor maior do que o número de índices na Tupla a impressão retornará com um erro

# Como já sabemos a função len nos dá o tamanho, nessa caso da tupla, no caso de lanche com 4 índices

print(len(lanche)) #com a saída 4 

# Também é possível usarmos estruturas de repetição dentro de estruturas compostas como for e while. Exemplos:

for comida in lanche:
    print(comida) # com a saída abaixo:

# hamburguer
# Suco
# Bolo
# Pudim

#É possível também fazer um for até o valor máximo da tupla, por exemplo:
    
for contador in range(0, len(lanche)): #A instrução aqui é, para cada comida do índice zero, até o len(tamanho total)de lanche. A partir disso você pode decidir o que pedir para imprimir. Exemplos:
    print(lanche[contador]) #com a saída abaixo:

# amburguer
# Suco
# Bolo
# Pudim

# Para os casos em que seja necessário apresentar em que posição determinado elemento está, podemos usar as estruturas abaixo:

for contador in range(0, len(lanche)): 
    print(f'Na posição {contador} encontramos o {lanche[contador]}') # ou ainda:

for posição, comida in enumerate(lanche):
    print(f'Na posição {posição} encontramos o {comida}') # ambos os códigos tem a mesma saída demonstrada abaixo:

# Na posição 0 encontramos o hamburguer
# Na posição 1 encontramos o Suco
# Na posição 2 encontramos o Bolo
# Na posição 3 encontramos o Pudim    

# Até aqui imprimimos a lista conforme a ordem em que ela foi digitada, podemos mandar imprimir ela na ordem alfabética ou númerica para uma lista com números conforme abaixo:

print(sorted(lanche)) #com a saída abaixo: 

# ['Bolo', 'Hamburguer', 'Pudim', 'Suco'] Observação, notem que a saída traz os números entre colchetes ou seja, como a tupla é imutável o Python transformou ela em lista para ordenar.

# Podemos contar elementos dentro das tuplas conforme exemplos abaixo:

print(lanche.count('Pudim')) # com a seguinte saída 1

# Podemos ainda descobrir em qual posição determinado item está utilizando o função index() conforme abaixo:

print(lanche.index('Pudim')) # com a saída 3, ou seja o pudim está no índice 3 ou seja é o quarto elemente de uma lista que começa com 0

# Obs.: Para os casos em que temos mais de um valor igual, o index fará referência a primeira posição. Porém podemos utilizar uma técnica de deslocamento conforme visto abaixo

lanche = 'Pudim', 'Hamburguer', 'Suco', 'Bolo', 'Pudim'

# Na tupla acima temos 2x Pudim, um na posição 0 e outro na posição 4, se utilizarmos o index sem deslocamento teremos a saída 0, porém se mandarmos procurar a partir do primeiro índice então a saída será 4 que é a próxima posição onde Pudim aparece. Vejamos abaixo:

print(lanche.index('Pudim')) # com saída 0

print(lanche.index('Pudim',1)) # agora com saída 4 pois houve um deslocamente para buscar a partir do índice 1 ignorando o índice 0

# É possível também termos tuplas com dados variados conforme abaixo:

pessoa = ('Cesar', 39, 'M', 99.88)
print(pessoa) # com a saída ('Cesar', 39, 'M', 99.88)

# Por fim, podemos apagar uma tupla com o comando del conforme abaixo

del(pessoa)
print(pessoa) # a saída para isso será um erro de não definição "NameError: name 'pessoa' is not defined" pois a tupla foi apagada pelo del antes de print.