num = 0
soma = -999
qtd_num = -1
while num != 999:
    num = int(input('Digite um número: '))
    soma = soma + num
    qtd_num += 1
print(f'Você digitou {qtd_num} números até digitar 999, chegando a uma soma de {soma}')