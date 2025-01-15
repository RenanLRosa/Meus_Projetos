# Tuplas são imutáveis
lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi demais!!!')
for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}.')
print('Comi demais!!!')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')
print('Comi demais!!!')