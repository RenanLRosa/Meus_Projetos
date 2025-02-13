import pandas as pd

tabela = pd.read_csv('vendas.csv')
print(tabela.head())
media_precos = tabela['Preco_Unitario'].mean()
tot_venda = tabela['Total_Venda'].sum()
desv_padr = tabela['Total_Venda'].std()
variancia = tabela['Total_Venda'].var()
mediana = tabela['Preco_Unitario'].median()
print('-'*30)
print(f'A média do preço dos produtos é R${media_precos:.2f}\n'
      f'O total de vendas foi R${tot_venda:.2f}\n'
      f'O desvio padrão das vendas foi R${desv_padr:.2f}\n'
      f'A variância das vendas foi R${variancia:.2f}\n'
      f'A mediana foi R${mediana:.2f}')
print('-'*30)
print(tabela['Preco_Unitario'].describe())
print(tabela['Total_Venda'].describe())

