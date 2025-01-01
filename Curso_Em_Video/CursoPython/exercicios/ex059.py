escolha = None
while escolha != 5:
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    escolha = int(input('''MENU:
[1] Somar
[2] Multiplicar
[3] Qual o maior
[4] Selecionar novos números
[5] Sair do programa
'''))
    if escolha == 1:
        print(f'A soma dos dois valores é igual a {n1+n2}\n')
        while escolha != 5 and escolha is not None:
            continuar = input('Continuar? [S/N]\n')
            if continuar.upper() == 'N':
                escolha = 5
            elif continuar.upper() == 'S':
                escolha = None
            else:
                print('Código inválido, tente novamente.')
    elif escolha == 2:
        print(f'O produto dos dois valores é {n1*n2}\n')
        while escolha != 5 and escolha is not None:
            continuar = input('Continuar? [S/N]\n')
            if continuar.upper() == 'N':
                escolha = 5
            elif continuar.upper() == 'S':
                escolha = None
            else:
                print('Código inválido, tente novamente.')
    elif escolha == 3:
        if n1 > n2:
            print(f'O maior valor entre {n1} e {n2} é {n1}')
        elif n1 < n2:
            print(f'O maior valor entre {n1} e {n2} é {n2}')
        elif n1 == n2:
            print('Os valores digitados são iguais.')
        while escolha != 5 and escolha is not None:
            continuar = input('Continuar? [S/N]\n')
            if continuar.upper() == 'N':
                escolha = 5
            elif continuar.upper() == 'S':
                escolha = None
            else:
                print('Código inválido, tente novamente.')
    elif escolha == 4 or escolha == 5:
        continue
    else:
        print('Código inválido, tente novamente')
print('Espero que tenha sido útil, até logo.')