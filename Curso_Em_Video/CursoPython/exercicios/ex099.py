from random import randint
def analisa_maior(num):
    n_maior = None
    for n in num:
        if not n_maior:
            n_maior = n
        elif n_maior < n:
            n_maior = n
    print(n_maior)
maior = [randint(-999, 999), randint(-999, 999), randint(-999, 999), randint(-999, 999), randint(-999, 999), randint(-999, 999), randint(-999, 999)]
print(maior)
analisa_maior(maior)
