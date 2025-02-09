from modulos import ex107_moeda as moeda

preco = float(input('Digite o preço: '))
dec = float(input('Digite a porcentagem do desconto: '))
acres = float(input('Digite a porcentagem da inflação: '))
log = moeda.escolha()

print(f'O preço é R${preco:.2f}\n'
      f'A metade do preço é {moeda.metade(preco, log)}\n'
      f'o dobro do preço é {moeda.dobro(preco, log)}\n'
      f'O preço com desconto de {dec}% é {moeda.diminuir(preco, dec, log)}\n'
      f'O preço com acréscimo de {acres}% é {moeda.aumentar(preco, acres, log)}\n')
