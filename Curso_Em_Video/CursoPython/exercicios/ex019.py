import random
Aluno1 = input('Qual o nome do primeiro aluno? ')
Aluno2 = input('Qual o nome do segundo aluno? ')
Aluno3 = input('Qual o nome do terceiro aluno? ')
Aluno4 = input('Qual o nome do quarto aluno? ')
escolhido = random.randint(1, 4)
if(escolhido == 1):
    print('O aluno escolhido é o {}.'.format(Aluno1))
if(escolhido == 2):
    print('O aluno escolhido é o {}.'.format(Aluno2))
if(escolhido == 3):
    print('O aluno escolhido é o {}.'.format(Aluno3))
if(escolhido == 4):
    print('O aluno escolhido é o {}.'.format(Aluno4))
lista=[Aluno1,Aluno2,Aluno3,Aluno4]
print('O outro aluno escolhido é {}.'.format(random.choice(lista)))