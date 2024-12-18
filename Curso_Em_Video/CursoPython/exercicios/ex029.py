velocidade = float(input('Digite a velocidade do carro: '))
if velocidade <= 80:
    print('Você está dentro do limite de velocidade estipulado. ')
else:
    print('Você ultrapassou o limite de velocidade.\nPor conta disso será multado em R${:.2f}'.format((velocidade-80)*7))