l = float(input('Qual a largura da parede a ser pintada em metros? '))
a = float(input('Qual a altura da parede a ser pintada em metros? '))
if((l*a)%2 == 0):
    print('A área de uma parede com essas dimensões é igual a {} m² e serão precisos no mínimo {:.0f} litros de tinta para pinta-la'.format(l*a,(l*a)//2))
else:
    print('A área de uma parede com essas dimensões é igual a {} m² e serão precisos no mínimo {:.0f} litros de tinta para pinta-la'.format(l*a,((l*a)//2)+1))