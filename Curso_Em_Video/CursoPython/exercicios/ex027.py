nome = input('Digite o seu nome completo: ')
primeiro_espaço = nome.find(' ')
print('O seu primeiro nome é: {}'.format(nome[:primeiro_espaço]))
ultimo_espaço = nome.rfind(' ')
print('Seu último sobrenome é: {}'.format(nome[ultimo_espaço+1:]))