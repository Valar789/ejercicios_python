# Obtener la representacion inversa de una cadena de caracteres

palabra = 'python'
print(palabra[::-1])

for i in range(len(palabra) -1, -1, -1):
    print(palabra[i], end='')