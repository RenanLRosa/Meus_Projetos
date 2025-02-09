def leiaInt(mensagem):
    try:
        n = int(input(mensagem))
        return n
    except Exception as erro:
        print('Formato inválido. Erro de tipo: ', erro.__class__)
        return 'Erro'

def leiaFloat(mensagem):
    try:
        n = float(input(mensagem))
        return n
    except Exception as erro:
        print('Formato inválido. Erro de tipo: ', erro.__class__)
        return 'Erro'


n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número racional: ')
print(f'Você acabou de digitar os números {n1} e {n2}')