from datetime import date
ano_nascimento = int(input('Em que ano você nasceu? '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
if idade <= 9:
    print('Sua categoria é mirim.')
elif 9 < idade <= 14:
    print('Sua categoria é infantil')
elif 14 < idade <= 19:
    print('Sua categoria é junior')
elif 19 < idade <= 25:
    print('Sua categoria é sênior')
else:
    print("Sua categoria é master.")