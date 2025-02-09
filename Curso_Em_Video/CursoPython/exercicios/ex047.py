i = int(input('Onde a sequência começa? '))
f = int(input('Onde a sequência termina?'))
selecao = int(input('Você quer os números pares ou impares? (Digite 1 para impar e 2 para par)\n'))
if i%2 == 0:
    i_tipo = 'par'
else:
    i_tipo = 'impar'
if f%2 == 0:
    f_tipo = 'par'
else:
    f_tipo = 'impar'
if selecao == 1:
    selecao_tipo = 'impar'
    if i_tipo == 'par':
        if f_tipo == 'par':
            print('o primeiro número é {}, o último é {} e você quer os números {}es.'.format(i_tipo, f_tipo, selecao_tipo))
            for c in range (i+1, f, 2):
                print(c)
        else:
            print('o primeiro número é {}, o último é {} e você quer os números {}es.'.format(i_tipo, f_tipo, selecao_tipo))
            for c in range (i+1, f+1, 2):
                print(c)
    else:
        if f_tipo == 'par':
            print('o primeiro número é {}, o último é {} e você quer os números {}es.'.format(i_tipo, f_tipo, selecao_tipo))
            for c in range (i, f, 2):
                print(c)
        else:
            print('o primeiro número é {}, o último é {} e você quer os números {}es.'.format(i_tipo, f_tipo, selecao_tipo))
            for c in range (i, f+1, 2):
                print(c)
elif selecao == 2:
    selecao_tipo = 'par'
    if i_tipo == 'par':
        if f_tipo == 'par':
            print('o primeiro número é {}, o último é {} e você quer os números {}es.'.format(i_tipo, f_tipo, selecao_tipo))
            for c in range (i, f+1, 2):
                print(c)
        else:
            print('o primeiro número é {}, o último é {} e você quer os números {}es.'.format(i_tipo, f_tipo, selecao_tipo))
            for c in range (i, f, 2):
                print(c)
    else:
        if f_tipo == 'par':
            print('o primeiro número é {}, o último é {} e você quer os números {}es.'.format(i_tipo, f_tipo, selecao_tipo))
            for c in range (i+1, f+1, 2):
                print(c)
        else:
            print('o primeiro número é {}, o último é {} e você quer os números {}es.'.format(i_tipo, f_tipo, selecao_tipo))
            for c in range (i+1, f, 2):
                print(c)
else:
    print('Seleção inválida.')