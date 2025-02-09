from modulos import ex107_moeda as moeda

preco = float(input('Digite o preço: '))
acres = float(input('Digite a porcentagem da inflação: '))
dec = float(input('Digite a porcentagem do desconto: '))
log = moeda.escolha()

moeda.resumo(preco= preco, dcrs= dec, acrs= acres, log=log )