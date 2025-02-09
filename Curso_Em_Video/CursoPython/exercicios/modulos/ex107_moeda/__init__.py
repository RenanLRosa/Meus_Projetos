def aumentar(preco, aumento, form=False):
    aumento = aumento/100
    aumento += 1
    preco *= aumento
    if form:
        return moeda(preco)
    else:
        return preco

def diminuir(preco, decrescimo, form=False):
    decrescimo = decrescimo/100
    decrescimo = 1 - decrescimo
    preco *= decrescimo
    if form:
        return moeda(preco)
    else:
        return preco

def dobro(n, form=False):
    if form:
        return moeda(n*2)
    else:
        return n*2

def metade(n, form=False):
    if form:
        return moeda(n/2)
    else:
        return n/2

def moeda(preco):
    preco = f'{preco:.2f}'
    form = f'R${preco[:-3]},{preco[-2:]}'
    return form

def escolha():
    while True:
        log = input('Você quer os valores formatados? [S/N] ')
        if log.upper() == 'S':
            return True
        elif log.upper() == 'N':
            return False
        else:
            print('Escolha inválida. Tente novamente.')

def resumo(preco, acrs, dcrs, log):
    print('-'*35)
    print(f'{'Resumo do valor':^35}')
    print('-' * 35)
    if log:
        print(f'{'Preço analisado:':<25} {moeda(preco)}')
    else:
        print(f'{'Preço analisado:':<25} {preco}')
    print(f'{'Dobro do preço:':<25} {dobro(preco, log)}')
    print(f'{'Metade do preço:':<25} {metade(preco, log)}')
    print(f'{f'{acrs}% de aumento:':<25} {aumentar(preco, acrs, log)}')
    print(f'{f'{dcrs}% de decréscimo:':<25} {diminuir(preco, dcrs, log)}')
    print('-' * 35)