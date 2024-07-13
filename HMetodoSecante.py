def metodo_secante(f, x0, x1, tol, max_iter=100):
    """
    Encuentra una raiz de la función f usando el metodo de la secante.

    """

    for _ in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)

        if f_x0 == f_x1:
            raise ValueError("f(x0) y f(x1) son iguales. El metodo no puede continuar.")

        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        if abs(x2 - x1) < tol:
            return x2

        x0, x1 = x1, x2

    raise ValueError("El metodo no converge despues de {} iteraciones.".format(max_iter))

# Ejemplo de uso
f = lambda x: x**2 -4 # Funcion a integrar
x0=4 # Valor de x0
x1=3 # Valor de x1
tol =.01 # Este es el error, el cual tambien se conoce como e
raiz = metodo_secante(f, x0,x1,tol)
print(f"Raiz encontrada por el metodo de la secante: {raiz}")
