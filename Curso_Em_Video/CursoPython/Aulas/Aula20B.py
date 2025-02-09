def dobra(lst):
    for c in range (0, len(lst)):
        lst[c] = lst[c] * 2

valores = [3, 5, 7, 9, 4, 4, 3]
dobra(valores)
print(valores)