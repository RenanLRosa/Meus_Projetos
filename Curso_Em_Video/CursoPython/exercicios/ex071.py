valor = int(input('Que valor você quer sacar? '))
n_50 = 0
n_20 = 0
n_10 = 0
n_1 = 0
while True:
    if valor - 50 >= 0:
        n_50 += 1
        valor -= 50
    elif valor - 20 >= 0:
        n_20 += 1
        valor -= 20
    elif valor - 10 >= 0:
        n_10 += 1
        valor -= 10
    elif valor - 1 >= 0:
        n_1 += 1
        valor -= 1
    else:
        break
print(f'Você sacará:\n {n_50} notas de R$50,00;\n {n_20} notas de R$20,00;\n {n_10} notas de R$10,00;\n {n_1} notas de R$1,00;')
