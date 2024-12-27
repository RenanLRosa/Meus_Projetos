import datetime
ano_nascimento = int(input('Qual o seu ano de nascimento? '))
ano_atual = datetime.date.today().year
ano_alist = ano_nascimento + 18
if ano_alist > ano_atual:
    anos_faltam = ano_alist - ano_atual
    print('Ainda não está na hora de você se alistar, você deve fazer isso no ano {}, ou seja, daqui a {} anos.'.format(ano_alist,anos_faltam))
elif ano_alist == ano_atual:
    print('Está na hora de se alistar! Você deve fazer isso esse ano.')
elif ano_alist < ano_atual:
    anos_atraso = ano_atual - ano_alist
    print('Já passou da hora de você se alistar! Você deveria ter feito isso no ano {}, ou seja, está {} anos atrasado!'.format(ano_alist, anos_atraso))