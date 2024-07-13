import numpy as np
def cuadratura_gauss(f, a, b, n):
    """
    Aproxima la integral de f(x) desde a hasta b usando la cuadratura de Gauss con n puntos.
    """
    [x, w] = np.polynomial.legendre.leggauss(n)
    
    t = 0.5 * (x + 1) * (b - a) + a
    f_t = f(t)
    
    return 0.5 * (b - a) * np.sum(w * f_t)

# Ejemplo de uso
f = lambda x: np.exp(x**2)  # Funcion a integrar
b = 1.2  # Limite superior
a = .2  # Limite inferior
n = 2  # Numero de subintervalos
resultado = cuadratura_gauss(f, a, b, n)
print(f"Resultado del metodo de cuadraura de Gauss: {resultado}")
