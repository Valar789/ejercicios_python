# Ejercicio Calcular el volumen de una esfera apartir del radio dado.

from cmath import pi


r = float(input('ingrese el usuario :'))

volumen = 4/3 * pi * r ** 3

print(f'El volumen de la esfera es : {volumen}')