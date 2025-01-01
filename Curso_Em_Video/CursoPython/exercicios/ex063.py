n = int(input('Quantos termos da sequência de Fibonacci você quer ver? '))
print('0')
n -= 1
num = 1
num_a = 0
while n > 0:
    num_s = num
    print(num)
    num = num_a + num
    num_a = num_s
    n -= 1