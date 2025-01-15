numeros = int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: '))
print(f'O número 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O número três apareceu {numeros.count(3)} vez neste conjunto, aparencendo primeiro na posição {numeros.index(3)} desse.')
else:
    print('O número 3 não apareceu neste conjunto.')
print('Os números pares são: ', end='')
for n in numeros:
     if n%2 == 0:
        print(n, end= ' ')