import math
ang = float(input('Qual o ângulo? '))
rad_ang = math.radians(ang)
print('Quanto ao ângulo {}, seu seno é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}'.format(ang, math.sin(rad_ang), math.cos(rad_ang), math.tan(rad_ang)))