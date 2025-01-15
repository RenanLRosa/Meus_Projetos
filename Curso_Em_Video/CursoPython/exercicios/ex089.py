lista = list()
aluno = list()
notas = list()
while True:
    aluno.append(input('Qual o nome do aluno? '))
    notas.append(float(input('Qual a primeira nota do aluno? ')))
    notas.append(float(input('Qual a segunda nota do aluno? ')))
    aluno.append(notas[:])
    lista.append(aluno[:])
    aluno.clear()
    notas.clear()
    while True:
        escolha = input('Você quer continuar? [S/N] ')
        if escolha.upper() == 'S':
            break
        elif escolha.upper() == 'N':
            break
        else:
            print('Opção inválida. Tente novamente.')
    if escolha.upper() == 'N':
        break
print('-'*40)
for c in range (0, len(lista)):
    print(f'BOLETIM - {c} - {lista[c][0]}')
    print(f'Nota prova 1: {lista[c][1][0]}')
    print(f'Nota prova 2: {lista[c][1][1]}')
    print(f'Média: {(lista[c][1][0] + lista[c][1][1])/2}')
    if (lista[c][1][0] + lista[c][1][1])/2 >= 6:
        print('\nAPROVADO.')
    else:
        print('\nREPROVADO.')
    print('-'*40)
while True:
    ident = int(input('Mostrar as notas de qual aluno? (999 interrompe.): '))
    if ident == 999:
        break
    elif 0 <= ident <= len(lista)-1:
        print(f'As notas de {lista[ident][0]} são {lista[ident][1]}')
    else:
        print('Código inválido.')