idade = [None] * 7
maiores = 0
menores = 0
for c in range(0, 7):
    idade[c] = int(input(f'Qual a idade do indivíduo {c+1}? '))
    if idade [c] >= 18:
        maiores = maiores + 1
    else:
        menores = menores + 1
maiores_lista = [None] * maiores
menores_lista = [None] * menores
contador_maior = 0
contador_menor = 0
for c in range(0, 7):
    if idade [c] >= 18:
        maiores_lista[contador_maior] = idade[c]
        contador_maior = contador_maior + 1
    else:
        menores_lista[contador_menor] = idade[c]
        contador_menor = contador_menor + 1
print(f'Entre os indivíduos de idades {idade} existem {maiores} maiores, isso é, as idades {maiores_lista}, e {menores} menores, isso é, as idade {menores_lista}.')