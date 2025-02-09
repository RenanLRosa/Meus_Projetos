from random import randint
tabela = list()
jogador = dict()
for c in range (0,4):
    jogador['nome'] = input('Nome do jogador: ')
    jogador['dado'] = randint(1, 6)
    if len(tabela) == 0:
        tabela.append(jogador.copy())
    else:
        for p in range (0, len(tabela)):
            if jogador['dado'] <= tabela[-1]['dado']:
                tabela.append(jogador.copy())
                break
            elif jogador['dado'] >= tabela[p]['dado']:
                tabela.insert(p, jogador.copy())
                break
print('Resultados:')
print(f'O vencedor foi {tabela[0]['nome']} tirando o número {tabela[0]['dado']}')
print('Classificação:')
for c in range (1,5):
    print(f'{c}º Lugar: {tabela[c-1]['nome']} com {tabela[c-1]['dado']}')