nome = (input('Qual o seu nome? '))
if nome == 'Renan':
    print('Você tem um lindo nome!')
elif nome == 'Luana' or nome == 'Gustavo' or nome == 'Ravy':
    print('Seu nome é meia bomba.')
elif nome in ['Ana', 'Renata', 'Gertrude', 'Wanda']:
    print('1800?')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}.'.format(nome))