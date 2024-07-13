import numpy as num

def metodo_trapecio(f, a, b, n):
    """
    Aproxima la integral de f(x) desde a hasta b usando la regla del trapecio con n subintervalos.
    """
    h = (b - a) / n
    suma = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        suma += f(a + i * h)
    return suma * h

# Ejemplo de uso
f = lambda x: 1- num.exp(-2*x)# Funcion a integrar
b = 4  # Limite superior
a = 0  # Limite inferior
n = 4  # Numero de subintervalos
resultado = metodo_trapecio(f, a, b, n)
print(f"Resultado del metodo de  trapecios: {resultado}")

