from random import randint
print('=-='*10, f'\n{'VAMOS JOGAR PAR OU ÍMPAR':^30}\n' + '=-='*10)
vitorias = 0
while True:
    n = int(input('Digite um valor: '))
    escolha = input('Par ou ímpar? [P/I] ').upper()
    print('-'*30)
    n_pc = randint(0, 10)
    resultado = n_pc + n
    if resultado % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    print(f'Você jogou {n} e o computador jogou {n_pc}. Deu {resultado}.\n{'-'*30}')
    if escolha == 'P':
        if resultado == 'PAR':
            vitorias += 1
            print('Você Venceu!')
        else:
            'Você Perdeu.'
            break
    elif escolha == 'I':
        if resultado == 'PAR':
            print('Você perdeu.')
            break
        else:
            vitorias +=1
            print('Você venceu!')
    else:
        print('O jogo acabou porque você não sabe jogar.')
        break
    print('Vamos jogar novamente...')
print(f'O jogo acabou, você venceu {vitorias} vezes.')
