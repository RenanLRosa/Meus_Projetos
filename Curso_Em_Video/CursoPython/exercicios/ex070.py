print(f'-='*20, f'\n{'MERCADINHO':^40}\n{'-='*20}')
preco_soma = 0
qtd_1000 = 0
p_barato = 99999
n_barato = ''
while True:
    nome = input('Que produto você comprou? ')
    preco = float(input('Qual o preço desse produto? '))
    preco_soma += preco
    if preco >= 1000:
        qtd_1000 += 1
    if p_barato > preco:
        p_barato = preco
        n_barato = nome
    escolha = input('Você quer acrescentar mais coisas ao carrinho? [S/N] ').upper()
    if escolha == 'N':
        break
    print('-'*40)
print(f'O total ficou R${preco_soma:.2f} com {qtd_1000} produtos custando R$1000.00 ou mais. O produto mais barato foi o {n_barato} custando R${p_barato:.2f}')