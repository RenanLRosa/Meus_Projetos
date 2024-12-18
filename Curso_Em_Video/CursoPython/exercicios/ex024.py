cidade = input('Digite o nome de uma cidade: ')
cidade_dividida = cidade.lower().split()
print('Sua cidade começa com a palavra santo? {}'.format(cidade_dividida[0] == 'santo'))