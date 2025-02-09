distancia = float(input('Qual a distância até o seu destino em kilometro? '))
if distancia > 200:
    print('Sua viagem custará: R${:.2f}'.format(0.5*distancia))
else:
    print('Sua viagem custará: R${:.2f}'.format(0.45*distancia))