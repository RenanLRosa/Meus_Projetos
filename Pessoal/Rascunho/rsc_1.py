import pandas as pd

tabela = pd.read_csv('ex115_Arquivo.csv')
lista = [['Renan', 18]]
tabela = pd.concat([tabela, pd.DataFrame(lista, columns=tabela.columns)], ignore_index=True)
tabela.drop(labels=2, axis=0, inplace=True)
tabela.to_csv('ex115_Arquivo.csv', index=False)
print(tabela)
