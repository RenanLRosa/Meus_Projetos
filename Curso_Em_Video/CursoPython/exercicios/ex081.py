lista: list[int] = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    valido = 0
    while valido == 0:
        escolha = input('Você quer continuar? [S/N] ')
        if escolha.upper() == 'S':
            valido = 1
        elif escolha.upper() == 'N':
            break
        else:
            print('Opção inválida. Tente novamente.')
    if escolha.upper() == 'N':
        break
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} valores, são eles {lista}')
if 5 in lista:
    print(f'O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')