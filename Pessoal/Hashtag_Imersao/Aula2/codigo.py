#Passo 1: Importar a base de dados.

import pandas as pd
import plotly.express as px
tabela = pd.read_csv('cancelamentos.csv')

#Passo 2: Visualizar a base de dados (Entender a base + identificar problemas.)

tabela = tabela.drop(columns='CustomerID') #Se livra de valores nada a ver
print(tabela.info())

#Passo 3: Corrigir os problemas de base de dados (Tratamento de dados).

    #Valores vazios(Deletar linhas com valores vazios).
tabela = tabela.dropna() # NaN -> Not a Number(Valores vazios)

#Passo 4: Análise inicial -> Quantos clientes cancelaram e qual o % de clientes.

print(tabela['cancelou'].value_counts())

print(tabela['cancelou'].value_counts(normalize=True)) #Percentual.

#Passo 5: Análise da causa de cancelamento dos clientes (Comparar as colunas com a coluna de cancelamento).

    #Gráfico:

for coluna in tabela.columns:

    #Etapa 1: Criar gráfico
    grafico = px.histogram(tabela, x=coluna, color='cancelou', text_auto=True) #Pesquisar parametros pesquisando no google 'plotly histogram' e analisando os scripts.
        #Usuarios do contrato mensal sempre cancelam.
            #Criar promoções quue incentivem o plano anual
        #Usuários que ligam mais de 5 vezes pro call center cancelam
            #Quando um usuário liga 3 vezes pro call center, alerta vermelho.
        #Usuários que atrasaram mais de 20 dias cancelaram
            #Criar um alerta para quando o atraso do pagamento chegar a 15 dias.
    #Etapa 2: Exibir gráfico
    grafico.show()

# duracao_contrato -> diferente de mensal

condicao = tabela['duracao_contrato'] != 'Monthly'
tabela = tabela[condicao]

# ligacoes_callcenter -> <= 4

condicao = tabela['ligacoes_callcenter'] <= 4
tabela = tabela[condicao]

# dias_atraso -> <= 20

condicao = tabela['dias_atraso'] <= 20
tabela = tabela[condicao]

print(tabela['cancelou'].value_counts(normalize=True))