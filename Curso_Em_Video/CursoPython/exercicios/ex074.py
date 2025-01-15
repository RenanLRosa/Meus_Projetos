from random import randint
numeros = (randint(0, 999), randint(0, 999), randint(0, 999), randint(0, 999), randint(0, 999))
print(numeros)
print(f'O maior valor entre esses é o {max(numeros)} e o menor é {min(numeros)}')