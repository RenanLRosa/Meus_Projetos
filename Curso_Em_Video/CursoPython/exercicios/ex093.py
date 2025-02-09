jogador = dict()
jogador['nome'] = input('Digite o nome do jogador: ')
jogador['partidas'] = int(input(f'Digite o número de partidas jogadas por {jogador['nome']}: '))
jogador['gols'] = list()
jogador['total'] = 0
for c in range (1, + jogador['partidas'] + 1):
    jogador['gols'].append(int(input(f'Quantos gols ele fez na partida {c}: ')))
    jogador['total'] += jogador['gols'][c-1]
print('=-' * 30)
print(f'O jogador {jogador['nome']} fez {jogador['total']} gols em {len(jogador['gols'])} partidas.\n'
      f'Detalhes:\n')
for c in range (1, + jogador['partidas'] + 1):
    print(f'Partida {c}: {jogador['gols'][c-1]}')