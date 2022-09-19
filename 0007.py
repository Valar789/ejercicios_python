# Obtener la extension de un archivo especificado por el usuario

import py_compile


name_file = input('Ingrese el nombre del archivo: ')

parts_file = name_file.split('.')
print(parts_file[-1]) # la ultima posisicion
print(parts_file[1]) #posicion exacta donde esta ubicada en la lista

