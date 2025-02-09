andares = int(input('Quantos andares deve ter a torre de cartas? '))
andares_print = andares
cartas = 0
while(andares>0):
    cartas = cartas + andares*2 + andares - 1
    andares = andares-1
if(cartas%54 == 0):
    print('Um baralho de {} andares usará {} cartas, ou seja, precisará de {} baralhos.'.format(andares_print, cartas, cartas/54))
else:
    print('Um baralho de {} andares usará {} cartas, ou seja, precisará de {} baralhos.'.format(andares_print, cartas, (cartas // 54)+1))