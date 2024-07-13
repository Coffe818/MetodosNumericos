import numpy as np
line = '-------------------------------------------------------------------------'
funcion1 = lambda x3: round((-1+x3)/10,4)
funcion2 = lambda x1, x3: round((8-4*x1+4*x3)/12, 4)
funcion3 = lambda x1, x2: round((4-4*x1-4*x2)/10, 4)



ff1 = "(-1+x_3)/10"
ff2 = "(8-4x_1+4x_3)/12"
ff3 = "(4-4x_1-4x_2)/10"


def gaussSidel(funciones, tol=0.02):
    x1a = x2a = x3a = 0
    e1 = e2 = e3 = tol + 1
    i = 1
    while e1 >= tol or e2 >= tol or e3 >= tol:
        x1n = funciones[0](x3a)
        x2n = funciones[1](x1a, x3a)
        x3n = funciones[2](x1a, x2a)


        e1 = abs((x1n - x1a) / x1n)
        e2 = abs((x2n - x2a) / x2n)
        e3 = abs((x3n - x3a) / x3n)

        print(f"\nIteracion {i}; x1={x1a:.4f}; x2={x2a:.4f}; x3={x3a:.4f}")
        print(f' x1={ff1}={x1n:.4f}\n x2={ff2}={x2n:.4f}\n x3={ff3}={x3n:.4f}')
        print(f' e1= |(({x1n})-({x1a}))/{x1n}|={e1:.4f}\n e2=  |(({x2n})-({x2a}))/{x2n}| = {e2:.4f}\n e3=  |(({x3n})-({x3a}))/{x3n}| = {e3:.4f}')

        x1a = x1n
        x2a = x2n
        x3a = x3n      
        i += 1
    print(f'Los valores finales son : \n x1={x1n:.4f}\n x2={x2n:.4f}\n x3={x3n:.4f} ')

# Define varias funciones lambda
funciones = [funcion1, funcion2, funcion3] 

gaussSidel(funciones)