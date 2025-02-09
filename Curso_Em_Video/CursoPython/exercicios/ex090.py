aluno = dict()
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input('Média: '))
if aluno['media'] >= 6:
    aluno['situacao'] = 'aprovado'
else:
    aluno['situacao'] = 'reprovado'
print(f'O aluno {aluno['nome'].capitalize()}, com média {aluno['media']} foi {aluno['situacao']}.')