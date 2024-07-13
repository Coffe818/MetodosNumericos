import numpy as np
def metodo_biseccion(f, a, b, tol, max_iter=100):
    """
    Encuentra una raiz de la funcion f en el intervalo [a, b] usando el metodo de biseccion.
    """
    if f(a) * f(b) >= 0:
        raise ValueError("La funcion debe cambiar de signo en el intervalo [a, b].")
    
    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            return c
        
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    

# Ejemplo de uso
f = lambda x: np.exp(3*x) -4 # Funcion a integrar
a = 0  # Limite a (izquiera) (a,b)
b = 1  # Limite b (derecha)
tol =.01 # Este es el error, el cual tambien se conoce como e
raiz = metodo_biseccion(f, a, b,tol)
print(f"Raiz encontrada por el metodo de biseccion: {raiz}")
