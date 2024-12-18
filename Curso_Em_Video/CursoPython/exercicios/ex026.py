frase = input('Digite uma frase: ')
print('Na sua frase a letra A aparece {} vezes'.format(frase.lower().count('a')))
print('A primeira letra A aparece na posição {}, ou seja, é a {}º caractere.'.format(frase.lower().find('a'), frase.lower().find('a') + 1))
print('A última letra A aparece na posição {}, ou seja, é o {}º caractere.'.format(frase.lower().rfind('a'), frase.lower().rfind('a') + 1))