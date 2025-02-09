import pandas as pd
from str import teste_acento
from enforcado import printForca
from random import randint

print('-'*30)
print(f'{'Jogo da Forca':^30}')
print('-'*30)
palavras = pd.read_csv('palavras.csv')
index = randint(0, len(palavras) - 1)
palavra = palavras.iat[index, 0]
palavra_fix = palavra
tentativas = 6
palavra = teste_acento(palavra)
palavra_tent = ['_']*len(palavra)
while True:
        printForca(tentativas)
        print(''.join(palavra_tent))
        letra = input('Digite uma letra: ')
        palavra_remove = palavra
        while True:
                if letra in palavra_remove:
                        index_letra = palavra_remove.index(letra)
                        palavra_tent[index_letra] = palavra_fix[index_letra]
                        if index_letra == len(palavra_remove)-1:
                                break
                        palavra_remove = palavra_remove.replace(letra, '*', 1)
                elif letra in palavra:
                        break
                else:
                        tentativas -= 1
                        break
        if '_' not in palavra_tent:
                print(''.join(palavra_tent))
                vitoria = True
                break
        if tentativas == 0:
                printForca(tentativas)
                vitoria = False
                break
if vitoria:
        print(f'Você venceu! A palavra era {palavra_fix}')
else:
        print(f'Você perdeu! A palavra era {palavra_fix}')

