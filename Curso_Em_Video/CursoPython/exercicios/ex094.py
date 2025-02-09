dados_dict = dict()
dados_lista = list()
media = 0
for c in range (0, 999):
    dados_dict['nome'] = input('Nome: ').title()
    dados_dict['idade'] = int(input('Idade: '))
    while True:
        dados_dict['sexo'] = input('Sexo [M/F]: ').upper()
        if dados_dict['sexo'] == 'F' or dados_dict['sexo'] == 'M':
            break
        else:
            print('Escolha inválida. Tente novamente.')
    media += dados_dict['idade']
    dados_lista.append(dados_dict.copy())
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
media = media/len(dados_lista)
num_pessoas = len(dados_lista)
mulheres = list()
maiores = list()
for c in range(0, len(dados_lista)):
    if dados_lista[c]['sexo'] == 'F':
        mulheres.append(dados_lista[c]['nome'])
    if dados_lista[c]['idade'] >= media:
        maiores.append(dados_lista[c]['nome'])
print(f'A lista é composta por {num_pessoas} pessoas com {len(mulheres)} mulheres e {len(maiores)} pessoas com idade igual ou acima da média do grupo.\n'
      f'As mulheres são: {mulheres}\n'
      f'A média de idade é {media:.2f} e os mais velhos são: {maiores}')