tupla = ('aprender',
         'programar',
         'linguagem',
         'cursos',
         'python',
         'alfinete',
         'alabarda',
         'farsa',
         'futuro',
         'fomento')
for palavra in tupla:
    print(f'\nNa palavra {palavra.upper()} temos ', end='')
    for c in range (0, len(palavra)):
        if palavra[c] in 'aeiou':
            print(palavra[c], end= ' ')
