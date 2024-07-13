import numpy as np
def metodo_regla_falsa(f, a, b, tol=1e-6, max_iter=100):
    """
    Encuentra una raiz de la funcion f en el intervalo [a, b] usando el metodo de la regla falsa.
    """
    if f(a) * f(b) >= 0:
        raise ValueError("La funcion debe cambiar de signo en el intervalo [a, b].")
    
    for _ in range(max_iter):
        c = b - (f(b) * (b - a)) / (f(b) - f(a))
        if abs(f(c)) < tol:
            return c
        
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c


# Ejemplo de uso
f = lambda x: 5*x**3-5*x**2+6*x-2 # Funcion a integrar
a = 0 # Limite a (izquiera) (a,b)
b = 1  # Limite b (derecha)
tol =.01 # Este es el error, el cual tambien se conoce como e
raiz = metodo_regla_falsa(f, a, b)
print(f"Raiz encontrada por el método de la regla falsa: {raiz}")
