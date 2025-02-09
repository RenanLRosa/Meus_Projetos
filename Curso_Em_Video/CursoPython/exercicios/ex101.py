from datetime import date
def voto(data_nas):
    vota_log = None
    data = date.today().year
    idade = data - data_nas
    if 18 <= idade <= 70:
        vota_log = True
        return vota_log
    elif idade < 16:
        vota_log = False
        return vota_log
    return vota_log
data_nas = int(input('Digite seu ano de nascimento: '))
vota_log = voto(data_nas) 
if vota_log == None:
    print('Seu voto é opcional.')
elif vota_log:
    print('Seu voto é obrigatório.')
else:
    print('Você ainda não pode votar.')

