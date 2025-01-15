lista = list()
dado = list()
while True:
    dado.append(input('Digite o nome: '))
    dado.append(float(input('Digite o peso: ')))
    lista.append(dado[:])
    escolha = input('Você quer continuar? [S/N]')
    if escolha.upper() == 'N':
        break
    dado.clear()
print(f'Foram cadastradas {len(lista)} pessoas.')
while True:
    qtd_lista = int(input('Digite o tamanho da lista de pessoas mais leves e pesadas que você quer ver.'))
    if 1 <= qtd_lista <= len(lista):
        break
    else:
        print('Valor inválido. Tente novamente.')
lista_leve = list()
lista_pesada = list()
for c in range (0, len(lista)):
    if len(lista_leve) == 0:
        lista_leve.append(lista[c])
    elif lista[c][1] > lista_leve[len(lista_leve)-1][1]:
        lista_leve.append(lista[c])
    else:
        for cont in range(0, len(lista_leve)):
            if lista_leve[cont][1] >= lista[c][1]:
                lista_leve.insert(cont, lista[c])
                break
print(lista_leve)
for c in range (0, len(lista_leve)):
    lista_pesada.append(lista_leve[-1 -c])
print(f'As {qtd_lista} pessoas mais leves são:', end=' ')
for c in range (0, qtd_lista):
    print(f'{lista_leve[c][0]} com {lista_leve[c][1]} kilos; ', end='')
print()
print(f'As {qtd_lista} pessoas mais pesadas são:', end=' ')
for c in range (0, qtd_lista):
    print(f'{lista_pesada[c][0]} com {lista_pesada[c][1]} kilos; ', end='')