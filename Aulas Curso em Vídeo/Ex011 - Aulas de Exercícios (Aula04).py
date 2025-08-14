largura = float(input('Digite a largura da sua parede: '))
altura = float(input('Digite a altura da sua parede '))
cobertura = float(input('Digite qual a cobertura da sua tinta em m²: '))
print(f'Sua parede tem {largura*altura}m², para pintá-la inteira você vai precisar de: {largura*altura/cobertura}latas de tinta')