from random import randint

def sorteia(lista):
    numeros = [randint(0,99), randint(0,99), randint(0,99), randint(0,99), randint(0,99)]
    lista_polida = list()
    for n in numeros:
        lista_polida.append(lista[n])
    return lista_polida

def soma(lista):
    resultado = 0
    for n in lista:
        if n % 2 == 0:
            resultado += n
    return resultado

lista_bruta = list()
for c in range (0,100):
    lista_bruta.append(randint(0, 999))
lista_polida = sorteia(lista_bruta)
resultado_soma = soma(lista_polida)
print(lista_polida)
print(resultado_soma)