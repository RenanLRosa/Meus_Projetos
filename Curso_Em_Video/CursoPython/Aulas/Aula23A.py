try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'Infelizmente ocorreu um erro. Área do problema: {erro.__class__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre, muito obrigado.')