peso_maior = 0
peso_menor = 10000
for c in range (0, 5):
    peso = float(input('Qual o peso a ser análisado? '))
    if peso > peso_maior:
        peso_maior = peso
    if peso < peso_menor:
        peso_menor = peso
print(f'O maior peso entre os analisados é {peso_maior} e o menor é {peso_menor}')