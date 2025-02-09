import pandas as pd
import modulos.ex111_utilidadesCeV.moeda as md
try:
    tabela = pd.read_csv('ex115_Arquivo.csv')
except FileNotFoundError:
    tabela = pd.DataFrame(columns=['Nome', 'Idade'])
    tabela.to_csv('ex115_Arquivo.csv', index=False)
lista = list()
pessoa = list()
while True:
    print('-' * 40)
    print(f'{'MENU PRINCIPAL':^40}')
    print('-' * 40)
    escolha = input('1: Ver pessoas cadastradas\n'
                    '2: Cadastrar novas pessoas\n'
                    '3: Excluir pessoa\n'
                    '4: Sair do sistema\n')
    if escolha == '1':
        print('-'*40)
        print(f'{'PESSOAS CADASTRADAS':^40}')
        print('-'*40)
        print(tabela)
        print('-'*40)
    elif escolha == '2':
        while True:
            pessoa.append(input('Digite o nome da nova pessoa: '))
            pessoa.append(input('Digite a idade da nova pessoa: '))
            lista.append(pessoa)
            pessoa = []
            if not md.escolha_2('Você quer cadastrar outra pessoa?'):
                tabela = pd.concat([tabela, pd.DataFrame(lista, columns=tabela.columns)], ignore_index=True)
                tabela.to_csv('ex115_Arquivo.csv', index=False)
                lista = []
                break
    elif escolha == '3':
        while True:
            i_pessoa = int(input('Digite o indicador da pessoa a ser excluida: '))
            tabela = tabela.drop(labels=i_pessoa, axis=0)
            if not md.escolha_2('Você quer excluir outra pessoa?'):
                tabela.to_csv('ex115_Arquivo.csv', index=False)
                break
    elif escolha == '4':
        break
print('Obrigado pela visita!')
