# Crear un funcion para evaluar un numero y realizar un operacion.

def diferencia(n):
    """Calcula la diferencia del valor pasado como argumento

    Args:
       pasa como argumento un numero entero 

    Returns:
        resultado de la operacion en entero 
    """
    if n <= 15:
        return 15 - n
    else:
        return (15 - n ) * 2


print(diferencia(17))
print(diferencia(3))