galera = list()
dado = list()
for c in range (0 , 3):
    dado.append(input('Digite o nome: '))
    dado.append(int(input('Digite a idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)