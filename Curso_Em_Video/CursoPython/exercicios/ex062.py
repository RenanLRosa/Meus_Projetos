n1 = int(input('Insira o primeiro termo dessa PA: '))
r = int(input('Insira a razão dessa PA: '))
c = 0
escolha = None
while c < 10:
    print(f'Termo {c+1} = {n1 + c*r}')
    c += 1
while escolha != 2:
    escolha = input('Você quer continuar? [S/N] ')
    while escolha != 1 and escolha != 2:
        qtd_termos = 0
        if escolha.upper() == 'S':
            escolha = 1
            qtd_termos = int(input('Você quer ver mais quantos termos?'))
        elif escolha.upper() == 'N':
            escolha = 2
        else:
            print('Código inválido, tent e novamente')
    cont = c + qtd_termos
    while cont > c:
        print(f'Termo {c+1} = {n1 + c*r}')
        c += 1
