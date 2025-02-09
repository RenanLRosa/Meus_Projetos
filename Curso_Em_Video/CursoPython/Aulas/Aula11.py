#\033[0;33;44m
#style = 0 ====> 0 = nada;  1 = negrito;  4 = underline;  7 = negativo(fundo vai pra letra, letra vai pra fundo
#text = 33  ====> 30=branco ; 31=vermelho ; 32=verde ; 33=amarelo ; 34=azul ; 35=roxo ; 36=ciano ; 37=cinza
#back = 44 ====> 40=branco ; 41=vermelho ; 42=verde ; 43=amarelo ; 44=azul ; 45=roxo ; 46=ciano ; 47=cinza
print('\033[4;30;45mOlá, Mundo!\033[m')
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a,b))
nome = 'Renan'
print('Olá, prazer em te conhecer, {0}{1}{0}!!!'.format('\033[4;34m', nome))