from modulos import ex107_moeda as moeda

preco = float(input('Digite o preço: '))
dec = float(input('Digite a porcentagem do desconto: '))
acres = float(input('Digite a porcentagem da inflação: '))

print(f'O preço é R${preco:.2f}\n'
      f'A metade do preço é R${moeda.metade(preco):.2f}\n'
      f'o dobro do preço é R${moeda.dobro(preco):.2f}\n'
      f'O preço com desconto de {dec}% é R${moeda.diminuir(preco, dec):.2f}\n'
      f'O preço com acréscimo de {acres}% é R${moeda.aumentar(preco, acres):.2f}\n')
