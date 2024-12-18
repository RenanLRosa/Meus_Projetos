n = input('Digite algo:')
print(type(n))
#Métodos de teste de tipo, isso é, testando o valor recebido e devolvendo um valor bouleano
print('1. {}'.format(n.isalpha())) #Se o valor é alphabético
print('2. {}'.format(n.isnumeric())) #Se o valor é numérico
print('3. {}'.format(n.isalnum())) #Se o valor é alphanumérico
print('4. {}'.format(n.isupper())) #Se o valor está em caixa alta
print('5. {}'.format(n.islower())) #Se o valor está todo minúsculo