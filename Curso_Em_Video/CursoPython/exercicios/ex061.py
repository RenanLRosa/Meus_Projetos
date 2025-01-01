n1 = int(input('Insira o primeiro termo dessa PA: '))
r = int(input('Insira a razão dessa PA: '))
n = [None] * 10
c = 0
while c < 10:
    n[c] = n1 + c*r
    c += 1
print(f'Os 10 primeiros termos dessa PA são {n}')