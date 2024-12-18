dias = int(input('Por quantos dias você usou o carro? '))
km = float(input('Quantos kilometros você rodou com o carro? '))
print('Você deve pagar por esse uso R${:.2f}'.format(60*dias+0.15*km))