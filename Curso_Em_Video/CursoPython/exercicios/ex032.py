from datetime import date
ano = int(input('Digite um ano, digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano%100 == 0:
    if ano%400 == 0:
        print('O ano {} é um ano bissexto.'.format(ano))
    else:
        print('O ano {} não é um ano bissexto.'.format(ano))
else:
    if ano%4 == 0:
        print('O ano {} é bissexto.'.format(ano))
    else:
        print('O ano {} não é bissexto.'.format(ano))