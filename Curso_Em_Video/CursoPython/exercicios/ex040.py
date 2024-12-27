n1 = float(input('Qual a primeira nota? '))
n2 = float(input('Qual a segunda nota? '))
media = (n1 + n2)/2
if media > 10 or media < 0:
    print('Só suportamos médias entre 0 e 10')
elif 7 <= media <= 10:
    print('Sua média é {}, ou seja, você está aprovado(a).'.format(media))
elif 5 <= media < 7:
    print('Sua média é {}, ou seja, você está de recuperação.'.format(media))
elif 0 <= media < 5:
    print('Sua média é {}, ou seja, você está reprovado(a).'.format(media))