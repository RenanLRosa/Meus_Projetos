expressao_str = input('Digite uma expressão: ')
expressao = list()
for c in range (0, len(expressao_str)):
    expressao.append(expressao_str[c])
valido = True
while True:
    if expressao.count('(') != 0 and expressao.count(')') != 0:
        if expressao.count('(') == expressao.count(')'):
            if expressao.index('(') < expressao.index(')'):
                del_i = expressao.index('(')
                del_f = expressao.index(')')
                del expressao[del_i]
                del expressao[del_f - 1]
            else:
                valido = False
                break
        else:
            valido = False
            break
    else:
        break
if valido:
    print('Essa expressão é válida.')
else:
    print('Essa expressão é inválida.')