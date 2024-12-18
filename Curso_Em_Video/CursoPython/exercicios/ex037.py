num_inteiro = int(input('Digite um número inteiro: '))
base_conversao = int(input('Indique em qual base de conversão você quer este número(1 - Binário / 2 - octal / 3 - hexadecimal).'))
if base_conversao == 1:
    print('O número {} em binário é igual a {}'.format(num_inteiro, bin(num_inteiro)))
elif base_conversao == 2:
    print('O número {} em octal é igual a {}'.format(num_inteiro, oct(num_inteiro)))
elif base_conversao == 3:
    print('O número {} em hexadecimal é igual a {}'.format(num_inteiro, hex(num_inteiro)))
else:
    print('Seu número foi convertido com sucesso!\nResultado: Reinicia e faz direito.')