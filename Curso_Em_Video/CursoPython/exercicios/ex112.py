import modulos.ex111_utilidadesCeV.moeda as moeda
import modulos.ex111_utilidadesCeV.dado as dado

preco = dado.leiaDinheiro()
acres = float(input('Digite a porcentagem da inflação: '))
dec = float(input('Digite a porcentagem do desconto: '))
log = moeda.escolha()

moeda.resumo(preco= preco, dcrs= dec, acrs= acres, log=log )