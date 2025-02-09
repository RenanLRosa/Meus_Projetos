import math
catO=float(input('Qual o cateto oposto desse triângulo? '))
catA=float(input('Qual o cateto adjascente desse triângulo? '))
print('A hipotenusa de um triândulo de catetos {} e {} é {}.'.format(catO, catA, math.sqrt(catO**2 + catA**2)))