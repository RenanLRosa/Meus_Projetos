lista = [int(input('Digite um valor: ')),
         int(input('Digite um valor: ')),
         int(input('Digite um valor: ')),
         int(input('Digite um valor: ')),
         int(input('Digite um valor: ')),
         ]
lista_max = lista[:]
lista_min = lista[:]
deletados = 0
print('=-'*30)
num_max = max(lista)
num_min = min(lista)
print(f'Você digitou os valores {lista}')
print(f'O maior valor da lista foi {num_max} nas posições: ', end= '')
for c in range (0, len(lista)):
    if num_max in lista_max:
        print(f'...{lista_max.index(num_max) + deletados}', end=' ')
        deletados += lista_max.index(num_max) + 1
        del lista_max[:lista_max.index(num_max) + 1]
    else:
        break
print(f'\nO menor valor da lista foi {num_min} nas posições: ', end= ' ')
deletados = 0
for c in range (0, len(lista)):
    if num_min in lista_min:
        print(f'...{lista_min.index(num_min) + deletados}', end= ' ')
        deletados += lista_min.index(num_min) + 1
        del lista_min[:lista_min.index(num_min) + 1]
    else:
        break