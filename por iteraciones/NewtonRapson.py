import sympy as sp

ln = '-----------------------------------------------------------'

def newtonRapson(funcion, tol, x0):
    x = sp.symbols('x')
    fd = sp.diff(funcion(x), x)
    f = sp.lambdify(x, funcion(x))
    f_prime = sp.lambdify(x, fd)

    iterations = 0
    x_n = x0
    e = tol + 1  # Inicializar e mayor que tol para entrar en el bucle
    

    while e >= tol :
        iterations += 1
        fx_n = f(x_n)
        fdx_n = f_prime(x_n)
        x_n1 = x_n - fx_n / fdx_n
        e = abs((x_n1 - x_n)/x_n1)
        x_n = x_n1
        
        print(f"\n{ln}\nIteración {iterations}:")
        print(f"F(x_{iterations-1}) = {fx_n:.4f}")
        print(f"F'(x_{iterations-1}) = {fdx_n:.4f}")
        print(f"x_{iterations} = {x_n:.4f}")
        print(f"Error estimado e_{iterations} = {e:.4f}")


    print(f"\n{ln}\nLa raíz encontrada es: {x_n:.4f}")

# Ejemplo de uso
funcion = lambda x: x+x**2-40 +3*x**(-1) 
tolerancia = 0.01
x0 = 0.08  # Aproximación inicial

newtonRapson(funcion, tolerancia, x0)
