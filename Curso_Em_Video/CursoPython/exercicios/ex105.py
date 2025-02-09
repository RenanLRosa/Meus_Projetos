def analisa_notas(lista, sit):
    """

    :param lista: Uma lista de notas em float
    :param sit: Se quer mostrar a situação.
    :return: Um dicionário com diversas informações sobre os números da lista
    """
    soma = 0
    info = dict()
    info['Quantidade_Notas'] = len(lista)
    info['Maior_Nota'] = max(lista)
    info['Menor_Nota'] = min(lista)
    for n in lista:
        soma += n
    info['Média'] = f'{soma / len(lista):.2f}'
    if soma / len(lista) >= 7:
        info['situacao'] = 'Boa'
    elif soma / len(lista) >= 6:
        info['situacao'] = 'Razoável'
    else:
        info['situacao'] = 'Ruim'
    return info
notas = list()
while True:
    notas.append(float(input('Digite uma nota: ')))
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
tabela = analisa_notas(notas, sit=True)
print(tabela)
help(analisa_notas())