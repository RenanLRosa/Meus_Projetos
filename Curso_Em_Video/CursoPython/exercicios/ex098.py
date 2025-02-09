def contador(ini, fim, pas):
    if pas == 0:
        pas = 1
    elif pas <= 0:
        pas = pas * (-1)
    print('-'*30)
    print(f'O contador fará a contagem de {ini} até {fim} contando de {pas} em {pas}.')
    if ini > fim:
        pas = pas * (-1)
        fim -= 1
    else:
        fim += 1
    for c in range (ini, fim, pas):
        print(c)
contador(1, 10, 1)
contador(10, 0, -2)
while True:
    contador(int(input('Digite o início da contagem: ')), int(input('Digite o fim da contagem: ')), int(input('Digite o passo da contagem: ')))