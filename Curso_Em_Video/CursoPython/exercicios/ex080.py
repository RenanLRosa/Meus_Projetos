lista = list()
lista.append(int(input('Digite um valor: ')))
for c in range (0, 4):
    n = int(input('Digite um valor: '))
    for cont in range (0, len(lista)):
        if lista [cont] >= n:
            lista.insert(cont, n)
            print(f'Adicionado na posição {lista.index(n)} da lista.')
            break
        elif cont == len(lista) - 1:
            lista.append(n)
            print(f'Adicionado na posição {lista.index(n)} da lista.')
print(lista)
