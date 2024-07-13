
def metodo_simpson_1_3(f, a, b, n):
    """
    Aproxima la integral de f(x) desde a hasta b usando la regla de Simpson 1/3 con n subintervalos.
    n debe ser par.
    """

    h = (b - a) / n
    suma = f(a) + f(b)
    
    for i in range(1, n, 2):
        suma += 4 * f(a + i * h)
    
    for i in range(2, n-1, 2):
        suma += 2 * f(a + i * h)
    
    return suma * h / 3

# Ejemplo de uso
f = lambda x: 1/x # Funcion a integrar
b = 4  # Limite superior
a = 1  # Limite inferior
n = 6  # Numero de subintervalos
resultado = metodo_simpson_1_3(f, a, b, n)
print(f"Resultado del metodo de Simpson 1/3: {resultado}")
