valor_casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos você quer pagar essa casa? '))
prestacao = valor_casa/(anos*12)
if prestacao >= 0.3*salario:
    print('O seu empréstimo foi negado.')
else:
    print('O seu empréstimo foi aprovado.')