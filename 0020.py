#Emular el funcionamiento del producto en cadena.

def funcion_producto_cadena(cadena: str, repeticion: int):
    """
    Emula el funcionamiento del producto (*) de cadena.
    
    """
    
    resultado = ""
     
    for i in range(repeticion):
        resultado += cadena
        
    return resultado
print(funcion_producto_cadena('Hola', 3))
    
    

print()