n1 = input('Digite o primeiro valor: ')
print('O valor digitado é do tipo primitivo {} '.format(type(n1)))
n1 = int(n1)
n2 = input('Digite o segundo valor: ')
print('O valor digitado é do tipo primitivo {} '.format(type(n2)))
n2 = float(n2)
print('Os valores digitados agora são do tipo primitivo {} e {} respectivamente'.format(type(n1), type(n1)))
s = n1 + n2
print('A soma dos dois valores resulta em {} e esse valor é do tipo primitivo {}'.format(s, type(s)))