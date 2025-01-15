lista = []
for c in range (0,4):
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
print(f'Foram digitados os valores {sorted(lista)}')