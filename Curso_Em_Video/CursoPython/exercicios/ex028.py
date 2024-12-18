import random
num = random.randint(0,5)
resposta = int(input('Tente advinhar o número escolhido entre 0 e 5: '))
if num == resposta:
    print('Voce acertou!!!')
else:
    print('Você errou!!! \nTente novamente')