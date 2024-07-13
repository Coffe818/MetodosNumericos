import numpy as np
line = '-------------------------------------------------------------------------'
funcion1 = lambda x_2,x_3: round((7.85+0.1*x_2+0.2*x_3)/3,4)
funcion2 = lambda x_1, x_3: round((-19.3-0.1*x_1+0.3*x_3)/7, 4)
funcion3 = lambda x_1, x_2: round((71.4-0.3*x_1+0.2*x_2)/(-10), 4)



ff1 = "(7.85+0.1x_2+0.2x_3)/3"
ff2 = "(-19.3-0.1x_1+0.3x_3)/7"
ff3 = "(71.4-0.3x_1+0.2x_2)/(-10)"


def gaussSidel(funciones, tol=0.01):
    x1a = x2a = x3a = 0
    e1 = e2 = e3 = tol + 1
    i = 1
    while e1 >= tol or e2 >= tol or e3 >= tol:
        x1n = funciones[0](x2a,x3a)
        x2n = funciones[1](x1n,x3a)
        x3n = funciones[2](x1n,x2n)
    

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
    print(f'Los valores finales son : \n x1={x1n:.4f}\n x2={x2n:.4f}\n x3={x3n:.4f}')

# Define varias funciones lambda
funciones = [funcion1, funcion2, funcion3] 

gaussSidel(funciones)

