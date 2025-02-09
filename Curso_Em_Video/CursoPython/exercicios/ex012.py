print('Grande Promoção!!!\nTodos os produtos com 5% de desconto!!!')
pin = float(input('Digite o preço inicial do produto: '))
pfin = pin*0.95
print('Na grande promoção você deixará de pagar {:.2f} para pagar {:.2f} nesse produto\nUma economia de {:.2f}!!!'.format(pin, pfin, pin-pfin))