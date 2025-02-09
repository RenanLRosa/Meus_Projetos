n = [0, 0, 0, 0, 0, 0]
soma = 0
for c in range (0, 6):
    n[c] = float(input('Digite um número: '))
    if n[c] % 2 == 0:
        soma = soma + n[c]
print(f'A soma dos valores pares entre os números {n} é igual a {soma}')