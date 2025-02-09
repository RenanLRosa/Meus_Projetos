import pyautogui
from time import sleep
import pandas
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.PAUSE = 0.5
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.click(x=733, y=651)
pyautogui.write(link)
pyautogui.press('enter')
sleep(1)
pyautogui.press('tab')
pyautogui.write('renan@gmail.com')
pyautogui.press('tab')
pyautogui.write('batatadoce')
pyautogui.press('tab')
pyautogui.press('enter')
sleep(3)
pyautogui.click(x=1174, y=454)
tabela = pandas.read_csv('produtos.csv')
print(tabela)
for linha in tabela.index:
    pyautogui.click(x=728, y=329)
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    if str(tabela.loc[linha]['obs']) != 'nan':
        pyautogui.write(str(tabela.loc[linha, 'obs']))
        pyautogui.press('tab')
    else:
        pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(10000)