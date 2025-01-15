pessoas = {'nome' : 'Gustavo', 'sexo' : 'M', 'idade' : 22}
print(f'O {pessoas['nome']} tem {pessoas['idade']} anos.')
pessoas['peso'] = 70.2
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())
for k, v in pessoas.items():
    print(f'{k} = {v}')