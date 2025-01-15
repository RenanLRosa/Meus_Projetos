print('-'*50)
print(f'{'LISTAGEM DE PREÇOS':^50}')
print('-'*50)
preços = ('Lápis', 1.75,
          'Borracha', 2,
          'Caderno', 15.90,
          'Estojo', 25,
          'Transferidor', 4.2,
          'Compasso', 9.99,
          'Mochila', 120.32,
          'Canetas', 22.3,
          'Livro', 34.90)
for c in range (0, len(preços), 2):
    print(f'{preços[c]:.<41}R${preços[c+1]:>7.2f}')
print('-'*50)