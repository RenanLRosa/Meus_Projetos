import random
contador = 3
vitorias = 0
empates = 0
derrotas = 0
print('JOKENPO!!!')
while contador > 0:
    num = random.randint(0,2)
    if num == 0:
        escolha_computador = 'pedra'
    if num == 1:
        escolha_computador = 'papel'
    if num == 2:
        escolha_computador = 'tesoura'
    escolha_player = input('Escolha e digite entre(pedra, papel e tesoura): ').lower()
    if num == 0:
        if escolha_player == 'pedra':
            print('O computador escolheu: {}'.format(escolha_computador))
            print('Empate!!!')
            empates = empates + 1
            contador = contador - 1
        if escolha_player == 'papel':
            print('O computador escolheu: {}'.format(escolha_computador))
            print('Vitória!!!')
            vitorias = vitorias + 1
            contador = contador - 1
        if escolha_player == 'tesoura':
            print('O computador escolheu: {}'.format(escolha_computador))
            print('Derrota!!!')
            derrotas = derrotas + 1
            contador = contador - 1
    if num == 1:
        if escolha_player == 'pedra':
            print('O computador escolheu: {}'.format(escolha_computador))
            print('Derrota!!!')
            derrotas = derrotas + 1
            contador = contador - 1
        if escolha_player == 'papel':
            print('O computador escolheu: {}'.format(escolha_computador))
            print('Empate!!!')
            empates = empates + 1
            contador = contador - 1
        if escolha_player == 'tesoura':
            print('O computador escolheu: {}'.format(escolha_computador))
            print('Vitória!!!')
            vitorias = vitorias + 1
            contador = contador - 1
    if num == 2:
        if escolha_player == 'pedra':
            print('O computador escolheu: {}'.format(escolha_computador))
            print('Vitória!!!')
            vitorias = vitorias + 1
            contador = contador - 1
        if escolha_player == 'papel':
            print('O computador escolheu: {}'.format(escolha_computador))
            print('Derrota!!!')
            derrotas = derrotas + 1
            contador = contador - 1
        if escolha_player == 'tesoura':
            print('O computador escolheu: {}'.format(escolha_computador))
            print('Empate!!!')
            empates = empates + 1
            contador = contador - 1
print('O placar final foi {} empates, {} derrotas e {} vitórias'.format(empates, derrotas, vitorias))
