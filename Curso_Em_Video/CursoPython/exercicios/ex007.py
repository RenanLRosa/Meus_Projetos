Nnotas = int(input('Digite o número de notas a ser analisadas: '))
Ntot=0
Ptot=0
while(Nnotas>0):
    nota = float(input('Digite a nota: '))
    peso = float(input('Digite o peso dessa nota: '))
    Ntot = Ntot + nota*peso
    Ptot = Ptot + peso
    Nnotas = Nnotas-1
print('A média dessas notas é igual a {:.2f}.'.format(Ntot/Ptot))