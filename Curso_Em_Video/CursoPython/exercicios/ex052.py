num = int(input('Digite um número. '))
primo = True
for c in range (2, num):
    if num % c == 0:
        primo = False
if primo:
    print(f'O número {num} é um número primo.')
else:
    print(f'O número {num} não é um número primo.')