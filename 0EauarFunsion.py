import numpy as np
import sympy as sp

def evaluar_funcion(f, x):
    return f(x)

def derivadas(f, x_val):
    x = sp.symbols('x')  
    # Definir la función y sus derivadas
    func_expr = f(x)
    df_expr = sp.diff(func_expr, x)
    d2f_expr = sp.diff(df_expr, x)

    # Convertir a funciones de Python
    df_lambda = sp.lambdify(x, df_expr, "numpy")
    d2f_lambda = sp.lambdify(x, d2f_expr, "numpy")

    dfx = df_lambda(x_val)
    d2fx = d2f_lambda(x_val)

    return df_expr, dfx, d2f_expr, d2fx

# Ejemplo de uso
f_sympy = lambda x: 5*x**3-5*x**2+6*x-2
x_val = 1

# Convertir la función a una función lambda de numpy para evaluar
f_numpy = sp.lambdify(sp.symbols('x'), f_sympy(sp.symbols('x')), "numpy")

resultado = evaluar_funcion(f_numpy, x_val)
primera_derivada, primera_derivada_evaluada, segunda_derivada, segunda_derivada_evaluada = derivadas(f_sympy, x_val)

print(f"El resultado de la función es {resultado}")
print(f"La primera derivada es {primera_derivada} y evaluada en {x_val} es {primera_derivada_evaluada}")
print(f"La segunda derivada es {segunda_derivada} y evaluada en {x_val} es {segunda_derivada_evaluada}")
