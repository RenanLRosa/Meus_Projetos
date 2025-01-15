
tabela = (
    "Botafogo",
    "Palmeiras",
    "Flamengo",
    "Fortaleza",
    "Internacional",
    "São Paulo",
    "Corinthians",
    "Bahia",
    "Cruzeiro",
    "Vasco da Gama",
    "Vitória",
    "Atlético Mineiro",
    "Fluminense",
    "Grêmio",
    "Red Bull Bragantino",
    "Juventude",
    "Athletico Paranaense",
    "Criciúma",
    "Atlético Goianiense",
    "Cuiabá"
)
print('-'*30)
print(tabela)
print('-'*30)
for c in range (0, len(tabela)):
    print(f'{c+1}º - {tabela[c]}')
print('-'*30)
print(f'Os primeiros 5 colocados são: {tabela[:5]}')
print('-'*30)
print(f'Os 4 ultimos 4 colocados são: {tabela[-4:]}')
print('-'*30)
print(f'Os times em ordem alfabética são: {sorted(tabela)}')
print('-'*30)
print(f'O internacional ficou em: {tabela.index('Internacional')+1}º colocado')