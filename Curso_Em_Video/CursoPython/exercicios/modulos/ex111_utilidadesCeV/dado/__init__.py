def leiaDinheiro():
    while True:
        preco = input('Digite o preço: ')
        validador = preco
        if preco.count('.') == 1:
            validador = preco.replace('.', '')
        if preco.count(',') == 1:
            validador = preco.replace(',', '')
            preco = preco.replace(',', '.')
        if validador.isnumeric():
            preco = float(preco)
            return preco
        else:
            print('Valor inválido. Tente novamente')
