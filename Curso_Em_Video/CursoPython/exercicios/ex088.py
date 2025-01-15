from random import randint
from time import sleep
apostas_total = list()
aposta = list()
print('-'*41)
print(f'{'JOGO NA MEGA SENA':^41}')
print('-'*41)
num = int(input('Quantos jogos você quer jogar? '))
print(f'-='*4, f'< SORTEANDO {num} NÚMEROS >', '=-'*4)
for c in range (0,num):
    for cont in range(0,6):
        n = randint(1, 60)
        if cont ==  0:
            aposta.append(n)
        elif n not in aposta:
            aposta.append(n)
    apostas_total.append(aposta[:])
    aposta.clear()
    print(f'Jogo {c + 1}: {apostas_total[c]}')
    sleep(0.5)