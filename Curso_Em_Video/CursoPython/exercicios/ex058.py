from random import randint
num = randint(1, 10)
palpite = 100
qtd_palpites = 0
while palpite != num:
    palpite = int(input('Qual o seu palpite? '))
    qtd_palpites += 1
    if palpite != num:
        print('Você errou. Tente novamente')
print(f'Você acertou em {qtd_palpites} tentativas.')