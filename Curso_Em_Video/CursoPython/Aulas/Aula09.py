frase = 'O Ravy roubou pão na casa do João'
print(frase[2])
print(frase[2:6])
print(frase[:6])
print(frase[21:])
print(frase[2:13:2])
print(frase[21::2])
print(len(frase))
print(frase.count('o', 0, 12))
print(frase.find('bou'))
print(frase.find('batata'))
print('Ravy' in frase)
print(frase.replace('pão','batata'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.split())
fraseSep=frase.split()
print('-'.join(fraseSep))
frase = '   Roubou pão  '
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
print("""Despencados de voos cansativos
Complicados e pensativos
Machucados após tantos crivos
Blindados com nossos motivos
Amuados, reflexivos
E dá-lhe antidepressivos
Acanhados entre discos e livros
Inofensivos""")