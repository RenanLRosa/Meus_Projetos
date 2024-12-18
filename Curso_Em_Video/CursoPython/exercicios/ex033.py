n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
if n1 >= n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1
if maior < n3:
    maior = n3
if menor > n3:
    menor = n3
print('O maior número desse conjunto é {} e o menor é {}'.format(maior,menor))