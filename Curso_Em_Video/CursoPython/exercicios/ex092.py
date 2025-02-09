import datetime
data = datetime.date.today().year
pessoa = {}
pessoa['nome'] = input('Digite seu nome: ') + ' '
pessoa['ano_nasc'] = int(input('Digite seu ano de nascimento: '))
pessoa['idade'] = data - pessoa['ano_nasc']
pessoa['clt'] = int(input('Digite sua carteira de trabalho(0 se não possui): '))
if pessoa ['clt'] != 0:
    pessoa['ano_contrat'] = int(input('Digite o ano da primeira contratação: '))
    pessoa['temp_contr'] = data - pessoa['ano_contrat']
    pessoa['temp_falta'] = 35 - pessoa['temp_contr']
    pessoa['salario'] = float(input('Digite o salário: '))
    pessoa['ano_apos'] = pessoa['ano_contrat'] + 35
    pessoa['idade_apos'] = pessoa['ano_apos'] - pessoa['ano_nasc']
    print(f'INFORMAÇÕES TRABALHISTAS- {pessoa['nome'].title()}- CTPS: {pessoa['clt']}\n'
          f'Ano de nascimento: {pessoa['ano_nasc']} ({pessoa['idade']} anos).\n'
          f'Ano de contratação: {pessoa['ano_contrat']} ({pessoa['temp_contr']} anos de contribuição).\n'
          f'Salário: {pessoa['salario']}\n'
          f'Aposentaria: {pessoa['nome'].title()[:pessoa['nome'].index(' ')]} tem {pessoa['temp_contr']} anos de contribuição, faltando {pessoa['temp_falta']} anos, assim, se aposentará no ano {pessoa['ano_apos']} quando tiver {pessoa['idade_apos']} anos de idade.')
else:
    print(f'{pessoa['nome']} tem {pessoa['idade']} anos e ainda não possui carteira de trabalho.')

