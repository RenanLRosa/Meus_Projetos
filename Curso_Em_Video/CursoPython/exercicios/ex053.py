frase = input('Digite uma frase.\n').lower()
frase_espaco = frase.replace(' ', '')
contador = len(frase_espaco) - 1
frase_nova = [None] * len(frase_espaco)
frase_lista = [None] * len(frase_espaco)
for c in range (0, len(frase_espaco)):
    frase_nova[c] = frase_espaco[contador]
    contador = contador - 1
    frase_lista[c] = frase_espaco[c]
if frase_lista == frase_nova:
    print(f'A frase {frase} é um palíndromo.')
else:
    print(f'A frase {frase} não é um palíndromo')
