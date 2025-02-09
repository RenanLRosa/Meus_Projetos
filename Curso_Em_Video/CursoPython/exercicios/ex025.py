nome = input('Digite seu nome: ')
if(nome.lower().find('silva') >= 0):
    resposta = 'Sim'
else:
    resposta = 'Não'
print('O nome {} carrega em si a palavra Silva? {}'.format(nome, resposta))
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))