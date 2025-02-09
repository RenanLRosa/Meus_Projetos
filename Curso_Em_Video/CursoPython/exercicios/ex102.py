def fatorial(num, show):
    '''num = fatorial de qual número
    show = se vai mostrar o fatorial'''
    fat = 1
    print(f'Após os calculos, o fatorial de {num} é igual a:')
    if show:
        for c in range(num, 0, -1):
            fat *= c
            print(f'{c}', end=' ')
            if c != 1:
                print('x ', end=' ')
        print(f'= {fat}')
    else:
        for c in range(num, 0, -1):
            fat *= c
        print(fat)


num = int(input('Você quer fazer  o fatorial de qual número? '))
while True:
    show = input('Você quer exibir o processo desse fatorial?[S/N] ').upper()
    if show == 'S':
        show = True
        break
    elif show == 'N':
        show = False
        break
    else:
        print('Valor inválido, tente novamente.')
fatorial(num, show)
