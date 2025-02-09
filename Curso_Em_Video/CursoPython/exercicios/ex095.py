jogadores = list()
jogador = dict()
while True:
    jogador['nome'] = input('Digite o nome do jogador: ')
    jogador['partidas'] = int(input(f'Digite o número de partidas jogadas por {jogador['nome']}: '))
    jogador['total'] = 0
    jogador['gols'] = list()
    for c in range (1, + jogador['partidas'] + 1):
        jogador['gols'].append(int(input(f'Quantos gols ele fez na partida {c}: ')))
        jogador['total'] += jogador['gols'][c-1]
    jogadores.append(jogador.copy())
    jogador.clear()
    while True:
        escolha = input('Você quer continuar? [S/N]')
        if escolha.upper() == 'S':
            break
        elif escolha.upper() == 'N':
            break
        else:
            print('Escolha inválida. Tente novamente.')
    if escolha.upper() == 'N':
        break
print('=-'*30)
print(f'{'CadeiraScore':^60}')
print('=-'*30)
for c in range(0, len(jogadores)):
    print(f'{c+1} - O jogador {jogadores[c]['nome']} fez {jogadores[c]['total']} gols em {len(jogadores[c]['gols'])} partidas - Uma média de {jogadores[c]['total'] / len(jogadores[c]['gols'])} gols por jogo')
print('=-'*30)
while True:
    num = int(input('Você quer os detalhes da campanha de qual jogador(0 para encerrar)? '))
    if num == 0:
        print('Obrigado pela visita!')
        break
    print('=-'*30)
    print(f'Campanha do {jogadores[num-1]['nome']}')
    for c in range(1, + jogadores[num-1]['partidas'] + 1):
        print(f'Partida {c}: {jogadores[num-1]['gols'][c - 1]}')