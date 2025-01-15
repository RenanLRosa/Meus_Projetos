lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    while True:
        escolha = input('Você quer continuar? [S/N] ')
        if escolha.upper() == 'S':
            break
        elif escolha.upper() == 'N':
            break
        else:
            print('Opção inválida. Tente novamente.')
    if escolha.upper() == 'N':
        break
lista_par = list()
lista_impar = list()
for c in range (0, len(lista)):
    if lista[c]%2 == 0:
        lista_par.append(lista[c])
    else:
        lista_impar.append(lista[c])
print(f'Dentre os valores digitados {lista}, os valores pares são {lista_par} e os impares são {lista_impar}')