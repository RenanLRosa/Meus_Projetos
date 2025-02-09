for c in range(1,6):
    print('Oi', c)
print('FIM')
for c in range(0,6):
    print('Oi', c)
print('FIM')
for c in range(6, -1, -1):
    print(c)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')