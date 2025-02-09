num = input('digite um número: ')
numFormatado = '{:0>4}'.format(num)
print('Unidade: {}'.format(numFormatado[3]))
print('Dezena: {}'.format(numFormatado[2]))
print('Centena: {}'.format(numFormatado[1]))
print('Milhar: {}'.format(numFormatado[0]))
num = int(num)
milhar = num//1000
centena = (num - (num//1000*1000))//100
dezena = (num - (milhar*1000 + centena*100))//10
unidade = (num - (milhar*1000 + centena*100 + dezena*10))
print("Unidade: {}".format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))
