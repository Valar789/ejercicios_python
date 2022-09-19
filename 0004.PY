#Solicitar el valor del radio de un circulo para calcular su area


from cmath import pi


valor_radio= int(input('ingresa radio: '))

area = pi * valor_radio ** 2

print(f'el area es {area}')