n1 = float(input('Qual será o primeiro termo da PA? '))
r = float(input('Qual será a razão da PA? '))
pa = [None] * 10
for c in range(0, 10):
    pa[c] = n1 + c * r
print(f'Os primeiros 10 termos dessa PA são: {pa}')
