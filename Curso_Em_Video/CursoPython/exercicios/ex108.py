from modulos import ex107_moeda as moeda

preco = float(input('Digite o preço: '))
dec = float(input('Digite a porcentagem do desconto: '))
acres = float(input('Digite a porcentagem da inflação: '))

print(f'O preço é {preco:.2f}\n'
      f'A metade do preço é {moeda.moeda(moeda.metade(preco))}\n'
      f'o dobro do preço é {moeda.moeda(moeda.dobro(preco))}\n'
      f'O preço com desconto de {dec}% é {moeda.moeda(moeda.diminuir(preco, dec))}\n'
      f'O preço com acréscimo de {acres}% é {moeda.moeda(moeda.aumentar(preco, acres))}\n')
