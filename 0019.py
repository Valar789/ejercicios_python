#Comprobar si una cadena termina con la extension .py, si no es asi, agregar la extension.

def validar_nombre_archivo(nombre_archivo):
    
    """
    Valida si un nombre de archivo tiene la extension .py
    si el archivo no tiene la extension la agrega
    """
    
    
    if len(nombre_archivo) >= 3 and nombre_archivo[-3:] == '.py':
        return nombre_archivo
    
    return nombre_archivo + '.py'

print(validar_nombre_archivo('main'))
print(validar_nombre_archivo('tiene.py'))