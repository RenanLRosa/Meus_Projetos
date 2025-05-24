import pandas as pd

tabela = pd.read_excel('vendas_exemplo.xlsx')
media_preco = tabela['Preco_Unitario'].drop_duplicates().mean()
maior_preco = tabela['Preco_Unitario'].idxmax()
menor_preco = tabela['Preco_Unitario'].idxmin()
tabela_som = tabela.groupby(['Produto'])['Quantidade'].sum()
mais_vend = tabela_som.idxmax()
print(tabela_som )