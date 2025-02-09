num = [2,5,9,1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop()
print(num)
print(f'Essa lista tem {len(num)} elementos')

valores = list()
valores.append(5)
valores.append(4)
valores.append(7)
for c, v in enumerate(valores):
    print(f'Na posição {c} eu encontrei o valor {v}!')