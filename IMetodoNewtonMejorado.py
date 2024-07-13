import sympy as sp

def newton_raphson_mejorado(f, tol, x0, max_iter=100):
    """
    Metodo de Newton-Raphson mejorado para encontrar la raiz de una funcion.

    """

    x = sp.symbols('x')

    # Definir la función y sus derivadas
    func_expr = f(x)
    df_expr = sp.diff(func_expr, x)
    d2f_expr = sp.diff(df_expr, x)

    # Convertir a funciones de Python
    f_lambda = sp.lambdify(x, func_expr)
    df_lambda = sp.lambdify(x, df_expr)
    d2f_lambda = sp.lambdify(x, d2f_expr)

    x_current = x0

    for i in range(max_iter):
        fx = f_lambda(x_current)
        dfx = df_lambda(x_current)
        d2fx = d2f_lambda(x_current)

        if dfx == 0:
            raise ValueError("La derivada es cero en x = {}. El metodo no puede continuar.".format(x_current))

        
        x_new = x_current - ((fx * dfx) / (dfx**2 - (fx * d2fx)))

        # Verificar convergencia
        if abs((x_new - x_current)/x_new) < tol:
            return x_new, i + 1

        x_current = x_new


# Ejemplo de uso
f = lambda x: x**3 - 5*x**2 +7*x -3  # Funcion a encontrar la raiz
tol = .01  # Tolerancia
x0= 0 # Valor de x0 

# Ejecutar el metodo de Newton-Raphson mejorado

raiz, iteraciones = newton_raphson_mejorado(f, tol,x0)
print(f"La raiz encontrada es {raiz} despues de {iteraciones} iteraciones.")

