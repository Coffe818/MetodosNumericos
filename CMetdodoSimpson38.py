import numpy as num

def metodo_simpson_3_8(f, a, b, n):
    """
    Aproxima la integral de f(x) desde a hasta b usando la regla de Simpson 3/8 con n subintervalos.
    """
    
    h = (b - a) / n
    suma = f(a) + f(b)
    
    for i in range(1, n, 3):
        suma += 3 * f(a + i * h)
        suma += 3 * f(a + (i+1) * h)
    
    for i in range(3, n-1, 3):
        suma += 2 * f(a + i * h)
    
    return suma * 3 * h / 8

# Ejemplo de uso
f = lambda x: 1- num.exp(-2*x)# Funcion a integrar
b = 4  # Limite superior
a = 0  # Limite inferior
n = 5  # Numero de subintervalos
resultado = metodo_simpson_3_8(f, a, b, n)
print(f"Resultado del metodo de Simpson 3/8: {resultado}")
