preco_normal = float(input('Qual o preço do produto? '))
forma_pagamento = int(input('Qual será a forma de pagamento? '
                            '\nConsidere as possibilidades a seguir e indique o código em questão'
                            '\nÁ vista no dinheiro ou cheque, 10% de desconto!!! - 1'
                            '\nÁ vista no cartão, 5% de desconto!!! - 2'
                            '\nEm até 2 vezes no cartão, sem juros!!! - 3'
                            '\nEm 3 ou mais parcelas no cartão, juros de 20%!!! - 4\n'))
if forma_pagamento == 1:
    print('Por pagar a vista você pagará apenas R${:.2f} no produto cujo preço anterior era R${:.2f}'.format(preco_normal*0.9, preco_normal))
elif forma_pagamento == 2:
    print('Por pagar a vista você pagará apenas R${:.2f} no produto cujo preço anterior era R${:.2f}'.format(preco_normal*0.95, preco_normal))
elif forma_pagamento == 3:
    print('No parcelamento em 2 vezes você pagará o preço total do produto, isso é, R${:.2f}'.format(preco_normal))
elif forma_pagamento == 4:
    qnt_parcelas = int(input('Em quantas vezes você efetuará o parcelamento? '))
    preco_novo = preco_normal*1.2
    preco_parcelas = preco_novo/qnt_parcelas
    print('No parcelamento em {} vezes você pagará 20% de desconto, assim pagará R${:.2f} no total, divididos em {} parcelas de R${:.2f}'.format(qnt_parcelas, preco_novo, qnt_parcelas, preco_parcelas))
else:
    print('Código inválido.')