num = int(input('Digite um número: '))
c = 0
print('A tabuada do \n{:=^12}'.format(num))
while(c<=10):
    pri = '{} x {} = {}'.format(num, c, num*c)
    print('{:^12}'.format(pri))
    c = c+1