#Calcular la suma de tres numeros, e incluir una condicion de igualdad

def suma_numeros(a, b , c):
    """
    Calcula la suma de 3 numero, si lo tres numeros son iguales, la suma multiplica por 3
    """   
    
    suma = a + b + c
    
    if a == b and a == c:
        suma *= 3
        
    return suma

print(suma_numeros(2 ,2, 7))
print(suma_numeros(2, 2, 2))