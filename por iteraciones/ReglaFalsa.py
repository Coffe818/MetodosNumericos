import numpy as np
ln='-----------------------------------------------------------'
def regla_falsa(f, a, b, tol):
    e = tol+1
    xa = 0
    i = 0
    while e >= tol:
        i += 1
        fa = f(a)
        fb = f(b)
        xi = ((a * fb) - (b * fa)) / (fb - fa)
        fx = f(xi)
        print(f"\n{ln}\nIteración {i}: valor de i={i}\nValores: \na={a:.5f}, \nb={b:.5f},\nf(a)={fa:.5f}, \nf(b)={fb:.5f},\nxi={xi:.5f} \nf(xi)={fx:.5f}")

        if fx * fa < 0:
            b = xi
            intr='(a,xi)'
        else:
            a = xi
            intr='(xi,b)'
        e = abs(xi - xa)
        xa = xi
        
        print(f"\ne={e:.4f}, \nnuevo intervalo:{intr}, ({a:.5f}, {b:.5f})")
    
    print(f"\n{ln}\nSe alcanzó la tolerancia deseada. Solución aproximada: {xi:.5f}\n")

# Ejemplo de uso:
f = lambda x: x**3- np.exp(x)
a = 1
b = 2
tol = 0.001

regla_falsa(f, a, b, tol)
