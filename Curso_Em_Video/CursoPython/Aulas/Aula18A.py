teste = list()
teste.append('Gustavo')
teste.append('40')
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
pessoal = [['João', 19], ['Maria', 22], ['Joaquim', 13], ['Amanda', 17]]
for p in pessoal:
    print(f'{p[0]} tem {p[1]} anos')