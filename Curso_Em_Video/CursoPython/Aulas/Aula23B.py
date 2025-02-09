try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Ocorreu um erro no tipo do dado')
except ZeroDivisionError:
    print('É impossível dividir por zero.')
except KeyboardInterrupt:
    print('O usuário não digitou nada.')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre, muito obrigado.')