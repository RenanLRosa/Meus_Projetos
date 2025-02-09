def leiaInt(mensagem):
    while True:
        n = input(mensagem)
        if n.isnumeric():
            n = int(n)
            return n
            break
        else:
            print('Erro. Digite um número inteiro.')

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')