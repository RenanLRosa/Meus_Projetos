med1 = float(input('Digite a primeira medida: '))
med2 = float(input('Digite a segunda medida: '))
med3 = float(input('Digite a terceira medida: '))
if med1 + med2 > med3 and med1 + med3 > med2 and med2 + med3 > med1:
    print('Com essas três medidas você pode fazer um triângulo.')
else:
    print('Com essas três medidas é impossível fazer um triângulo.')