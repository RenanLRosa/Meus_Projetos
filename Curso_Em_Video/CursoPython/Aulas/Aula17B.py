a = [2, 3, 4, 7]
b = a
b[2] = 8  #Liga as duas listas
print(f'Lista A: {a}')
print(f'Lista B: {b}')
#Com as listas ligadas, quando eu mudo o valor de uma muda das duas.
c = [2, 3, 4, 7]
d = c[:]  #D recebe todos os valores de c(Uma cópia), sem ligar as duas.
d[2] = 8
print(f'Lista C: {c}')
print(f'Lista D: {d}')
