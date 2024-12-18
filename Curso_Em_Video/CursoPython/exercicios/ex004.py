valor = input('Digite algo: ')
if(valor.isnumeric()):
    valor = int(valor)
    print('Você digitou {} e isso é um número, isso é, do tipo primitivo {}'.format(valor, type(valor)))
elif(valor.isalnum()):
    let = ''
    if(valor.isupper()):
        let = ' e possui todas as letras maiúsculas,'
    if(valor.islower()):
        let = ' e possui todas as letras minúsculas,'
    if(valor.istitle()):
        let = ' e está capitalizado, '
    if(valor.isalpha()):
        print('Seu valor é um texto sem números,{} sendo do tipo primitivo {}'.format(let, type(valor)))
        print('Ou seja: ')
        print('Só tem espaços? {}'.format(valor.isspace()))
        print('É um número? {}'.format(valor.isnumeric()))
        print('É albético? {}'.format(valor.isalpha()))
        print('É alfanumérico? {}'.format(valor.isalnum()))
        print('Está em maiúsculas? {}'.format(valor.isupper()))
        print('Está em minúsculas? {}'.format(valor.islower()))
        print('Está capitalizado? {}'.format(valor.istitle()))
    else:
        print('Seu valor é um texto com números,{} sendo do tipo primitivo {}'.format(let, type(valor)))
        print('Ou seja: ')
        print('Só tem espaços? {}'.format(valor.isspace()))
        print('É um número? {}'.format(valor.isnumeric()))
        print('É albético? {}'.format(valor.isalpha()))
        print('É alfanumérico? {}'.format(valor.isalnum()))
        print('Está em maiúsculas? {}'.format(valor.isupper()))
        print('Está em minúsculas? {}'.format(valor.islower()))
        print('Está capitalizado? {}'.format(valor.istitle()))
else:
    print('Seu valor não está entre os valores que eu sei analisar')
    print('Entretanto: ')
    print('Só tem espaços? {}'.format(valor.isspace()))
    print('É um número? {}'.format(valor.isnumeric()))
    print('É albético? {}'.format(valor.isalpha()))
    print('É alfanumérico? {}'.format(valor.isalnum()))
    print('Está em maiúsculas? {}'.format(valor.isupper()))
    print('Está em minúsculas? {}'.format(valor.islower()))
    print('Está capitalizado? {}'.format(valor.istitle()))