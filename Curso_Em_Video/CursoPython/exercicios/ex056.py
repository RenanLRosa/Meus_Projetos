nome = [None]*4
sexo = [None]*4
idade = [None]*4
idade_soma = 0
mais_velho = 0
nome_velho = 'Não existem homens nessa faixa.'
menores_20 = 0
for c in range (0,4):
    nome[c] = input('Qual o nome do indivíduo? ')
    sexo[c] = int(input('Qual o sexo? (1 - Homem; 2 - Mulher;) '))
    idade[c] = int(input('Qual a idade? '))
    idade_soma = idade_soma + idade[c]
    if sexo[c] == 1:
        if idade[c] > mais_velho:
            mais_velho = idade[c]
            nome_velho = nome[c]
    elif idade[c] < 20:
        menores_20 = menores_20 + 1
    if sexo[c] == 1:
        sexo[c] = 'Homem'
    elif sexo[c] == 2:
        sexo[c] = 'Mulher'
    else:
        sexo[c] = 'Indisponível'
print(f'entre os indivíduos:')
for c in range (0,4):
    print(f'{nome[c]} - {sexo[c]} - {idade[c]} anos.')
print(f'A média de idade é {idade_soma/4:.2f} com {menores_20} mulheres abaixo de 20 anos e tendo o {nome_velho} como o homem mais velho, com {mais_velho} anos de idade')