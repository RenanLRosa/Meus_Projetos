num_lista = [None]
escolha = 0
c = 0
num_maior = -99999
num_menor = 999999
soma = 0
qtd = 0
while escolha != 1:
    escolha = None
    num_lista[c] = float(input('Digite um número: '))
    if num_maior < num_lista[c]:
        num_maior = num_lista[c]
    if num_menor > num_lista[c]:
        num_menor = num_lista[c]
    soma = soma + num_lista[c]
    qtd += 1
    c += 1
    while escolha != 1 and escolha != 0:
        escolha = input('Você quer continuar? [S/N] ')
        if escolha.upper() == 'S':
            escolha = 0
            num_lista += [None]
        elif escolha.upper() == 'N':
            escolha = 1
        else:
            print('Código inválido. Tente novamente.')
print(f'Os números que você digitou foram {num_lista}\nVocê digitou {qtd} números, somando {soma} e com uma média de {soma/qtd} por número.\nO maior número que você digitou foi {num_maior} e o menor foi {num_menor}')