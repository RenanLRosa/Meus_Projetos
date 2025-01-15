linha_1 = [int(input('Digite o valor a¹¹ da matriz: '))], [int(input('Digite o valor a¹² da matriz: '))], [int(input('Digite o valor a¹³ da matriz: '))]
linha_2 = [int(input('Digite o valor a²¹ da matriz: '))], [int(input('Digite o valor a²² da matriz: '))], [int(input('Digite o valor a²³ da matriz: '))]
linha_3 = [int(input('Digite o valor a³¹ da matriz: '))], [int(input('Digite o valor a³² da matriz: '))], [int(input('Digite o valor a³³ da matriz: '))]
matriz = linha_1, linha_2, linha_3
soma_par = 0
soma_coluna = 0
print('-='*30)
print(f'{matriz[0][0]} {matriz[0][1]} {matriz[0][2]} \n'
      f'{matriz[1][0]} {matriz[1][1]} {matriz[1][2]} \n'
      f'{matriz[2][0]} {matriz[2][1]} {matriz[2][2]} ')
for c in range(0,3):
    for cont in range(0,3):
        if max(matriz[c][cont]) % 2 == 0:
            soma_par+= max(matriz[c][cont])
        if cont == 2:
            soma_coluna += max(matriz[c][2])
print(f'A soma dos valores pares dessa matriz é igual a {soma_par}, a soma dos valores da terceira coluna é {soma_coluna} e o maior valor da segunda linha é {max(matriz[1])}')