qtd_18 = 0
qtd_h = 0
qtd_m20 = 0
while True:
    idade = int(input('Qual a idade do indivíduo? '))
    sexo = input('Qual o sexo do mesmo? [H/F] ').upper()
    if idade > 18:
        qtd_18 += 1
    if sexo == 'M':
        qtd_h += 1
    else:
        if idade < 20:
            qtd_m20 += 1
    escolha = input('Você quer continuar? [S/N] ').upper()
    if escolha == 'N':
        break
print(f'Nessa sequência de cadastros existem:\n{qtd_18} maiores de 18;\n{qtd_h} Homens;\n{qtd_m20} mulheres com menos de 20 anos.')