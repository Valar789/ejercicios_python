# Solicitar al usuario un numero n y luego calcular  n + nn + nnn

n = int(input('escriba el valor de n: '))
nn = int((f'{n}{n}'))
nnn= int((f'{n}{n}{n}'))

suma = n + nn + nnn

print(suma)

