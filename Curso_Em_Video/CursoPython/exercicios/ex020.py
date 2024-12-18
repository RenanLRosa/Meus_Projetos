import random
alunoA = input('Qual o nome do primeiro aluno? ')
alunoB = input('Qual o nome do segundo aluno? ')
alunoC = input('Qual o nome do terceiro aluno? ')
alunoD = input('Qual o nome do quarto aluno? ')
seq = [alunoA, alunoB, alunoC, alunoD]
print(random.sample(seq, k=len(seq)))
random.shuffle(seq)
print(seq)