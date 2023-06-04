import math

def muller(f, x0, x1, x2, max_iter):
    print("Iniciando método de Muller...")
    print("Valores iniciales: x0 = {:.6f}, x1 = {:.6f}, x2 = {:.6f}".format(x0, x1, x2))
    print("Número máximo de iteraciones:", max_iter)
    print()

    tol = 1e-6  # Tolerancia
    iter_count = 0 #Número de interacciones

    while iter_count < max_iter:
        iter_count += 1

        f0 = f(x0)
        f1 = f(x1)
        f2 = f(x2)
        h0 = x1 - x0
        h1 = x2 - x1
        s0 = (f1 - f0) / h0
        s1 = (f2 - f1) / h1

        print("Iteración", iter_count)
        print("+-------+--------+--------+--------+")
        print("|   x   |  f(x)  |   h    |   s    |")
        print("+-------+--------+--------+--------+")
        print("| {:.4f} | {:.4f} | {:.4f} | {:.4f} |".format(x0, f0, h0, s0))
        print("| {:.4f} | {:.4f} | {:.4f} | {:.4f} |".format(x1, f1, h1, s1))
        print("| {:.4f} | {:.4f} |".format(x2, f2))
        print("+-------+--------+--------+--------+")
        print()

        a = (s1 - s0) / (h1 + h0)
        b = a * h1 + s1
        c = f2

        if b >= 0:
            den = math.sqrt(b * b - 4 * a * c)
        else:
            den = math.sqrt(b * b + 4 * a * c)

        if abs(b - den) < abs(b + den):
            dx = h1 * (-2 * c) / (b + den)
        else:
            dx = h1 * (-2 * c) / (b - den)

        x3 = x2 + dx

        if abs(f(x3)) < tol:
            print("Raíz encontrada:", x3)
            return x3

        print("a = {:.6f}, b = {:.6f}, c = {:.6f}".format(a, b, c))
        print("Raíz +:", x3)
        print("Raíz -:", -x3)
        print()

        x0 = x1
        x1 = x2
        x2 = x3

    print("El método no converge después de", max_iter, "iteraciones.")
    return None

equation = input("Ingrese la función f(x): ")
f = lambda x: eval(equation.replace('^', '**'))

x0 = float(input("Ingrese el valor inicial x0: "))
x1 = float(input("Ingrese el valor inicial x1: "))
x2 = float(input("Ingrese el valor inicial x2: "))
max_iter = int(input("Ingrese el número máximo de iteraciones: "))

raiz = muller(f, x0, x1, x2, max_iter)

if raiz is not None:
    print("La raíz encontrada es:", raiz)
else:
    print("No se encontró raíz dentro del número máximo de iteraciones.")
