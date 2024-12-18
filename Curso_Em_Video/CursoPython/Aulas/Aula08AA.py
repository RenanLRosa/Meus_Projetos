#import BIBLIOTECA (Para importar todas as informações de uma biblioteca)
#from BIBLIOTECA import VALOR (para importar determinada informação de uma bibilioteca)
from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}.'.format(num, raiz))