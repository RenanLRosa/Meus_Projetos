peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso/(altura**2)
if 18.5 > imc:
    print('Você está abaixo do peso.')
elif 18.5 <= imc <= 25:
    print('Você está no peso ideal. ')
elif imc <= 30:
    print('Você está sobrepeso.')
elif imc <= 40:
    print('Você está obeso.')
else:
    print('Você sofre de obesidade mórbida.')