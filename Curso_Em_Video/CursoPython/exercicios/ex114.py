import requests
try:
    acesso = requests.get(url='https://www.youtube.com/')
    acesso.status_code
    print('O site está funcionando.')
except Exception as erro:
    print('O site está fora do ar. Erro: ', erro.__class__)