import sympy as sp

def newton_raphson(func_expr,tol, x0=1, max_iter=100):
    """
    Metodo de Newton-Raphson para encontrar la raiz de una funcion.

    """
    x = sp.symbols('x')
    func_expr = f(x)

    df_expr = sp.diff(func_expr, x)

    f_lambda = sp.lambdify(x, func_expr)
    df_lambda = sp.lambdify(x, df_expr)

    x_current = x0

    for i in range(max_iter):
        fx = f_lambda(x_current)
        dfx = df_lambda(x_current)

        if dfx == 0:
            raise ValueError("La derivada es cero en x = {}. El metodo no puede continuar.".format(x_current))

        x_new = x_current - fx / dfx

        if abs(x_new - x_current) < tol:
            return x_new, i + 1

        x_current = x_new

# Ejemplo de uso
f = lambda x: x**3 + 2*x - 4 # Funcion a integrar
tol =.00001 # Este es el error, el cual tambien se conoce como e


# Ejecutar el método de Newton-Raphson

raiz, iteraciones = newton_raphson(f, tol)
print(f"La raiz encontrada es {raiz} despues de {iteraciones} iteraciones.")

