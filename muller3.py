import math

def muller(f, x0, x1, x2, tol, max_iter):
    print("Iniciando método de Muller...")
    print("Valores iniciales: x0 =", x0, ", x1 =", x1, ", x2 =", x2)
    print("Tolerancia: ", tol)
    print("Número máximo de iteraciones: ", max_iter)
    print("")

    iter_count = 0

    while iter_count < max_iter:
        iter_count += 1

        h0 = x1 - x0
        h1 = x2 - x1
        s0 = (f(x1) - f(x0)) / h0
        s1 = (f(x2) - f(x1)) / h1

        print("Iteración ", iter_count)
        print("x0 =", x0, ", x1 =", x1, ", x2 =", x2)
        print("f(x0) =", f(x0), ", f(x1) =", f(x1), ", f(x2) =", f(x2))
        print("h0 =", h0, ", h1 =", h1)
        print("s0 =", s0, ", s1 =", s1)
        print("")

        a = (s1 - s0) / (h1 + h0)
        b = a * h1 + s1
        c = f(x2)

        if b >= 0:
            den = math.sqrt(b * b - 4 * a * c)
        else:
            den = math.sqrt(b * b + 4 * a * c)

        if abs(b - den) < abs(b + den):
            dx = h1 * (-2 * c) / (b + den)
        else:
            dx = h1 * (-2 * c) / (b - den)

        x3 = x2 + dx

        if abs(x3 - x2) < tol:  # Corregir esta línea
            print("Raíz encontrada:", x3)
            return x3

        x0 = x1
        x1 = x2
        x2 = x3

    print("El método no converge después de", max_iter, "iteraciones.")
    return None

equation = input("Ingrese la función: ")
f = lambda x: eval(equation.replace('^', '**'))

x0 = float(input("Ingrese el valor inicial x0: "))
x1 = float(input("Ingrese el valor inicial x1: "))
x2 = float(input("Ingrese el valor inicial x2: "))
tol = 1e-6
max_iter = 10  # Aumentar el número máximo de iteraciones

raiz = muller(f, x0, x1, x2, tol, max_iter)

if raiz is not None:
    print("La raíz encontrada es:", raiz)
else:
    print("No se encontró raíz dentro del número máximo de iteraciones.")
