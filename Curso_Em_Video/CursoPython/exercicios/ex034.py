salario = float(input('Digite o salário'))
if salario > 1.250:
    print('O novo salário, após acréscimos, é: R${:.2f}'.format(salario*1.1))
else:
    print('O novo salário, após acréscimos, é: R${:.2f}'.format(salario*1.15))