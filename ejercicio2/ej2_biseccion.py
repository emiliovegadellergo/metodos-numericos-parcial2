import math

# Definición de la función f(y) = e^(-y) - 4y
def f(y):
    return math.exp(-y) - 4 * y

def biseccion(a, b, tolerancia=1e-2, max_iter=100):
    # Verificar que el intervalo contiene una raíz (cambio de signo)
    if f(a) * f(b) >= 0:
        print("Error: f(a) y f(b) deben tener signos opuestos.")
        return None, 0

    print(f"{'Iter':>5}  {'a':>10}  {'b':>10}  {'c':>10}  {'f(c)':>10}  {'Error':>10}")
    print("-" * 62)

    iteracion = 0
    c_prev = a  # valor del punto medio anterior para calcular el error

    while iteracion < max_iter:
        # Calcular el punto medio del intervalo
        c = (a + b) / 2
        fc = f(c)

        # Error absoluto: distancia entre punto medio actual y anterior
        # En la primera iteración se usa la mitad del intervalo inicial
        if iteracion == 0:
            error = abs(b - a) / 2
        else:
            error = abs(c - c_prev)

        print(f"{iteracion + 1:>5}  {a:>10.5f}  {b:>10.5f}  {c:>10.5f}  {fc:>10.5f}  {error:>10.5e}")

        # Verificar criterio de paro por error absoluto
        if error < tolerancia:
            return c, iteracion + 1

        # Determinar en qué subintervalo está la raíz según el teorema de Bolzano
        if f(a) * fc < 0:
            # La raíz está en [a, c]
            b = c
        else:
            # La raíz está en [c, b]
            a = c

        c_prev = c
        iteracion += 1

    print("Se alcanzó el máximo de iteraciones sin converger.")
    return c, iteracion


if __name__ == "__main__":
    a = 0.1         # Extremo izquierdo del intervalo
    b = 0.3         # Extremo derecho del intervalo
    tolerancia = 1e-2

    print("=" * 62)
    print("  Método de Bisección")
    print("  f(y) = e^(-y) - 4y = 0")
    print(f"  Intervalo: [{a}, {b}],  tolerancia = {tolerancia}")
    print(f"  f({a}) = {f(a):.5f},  f({b}) = {f(b):.5f}")
    print("=" * 62)

    raiz, num_iter = biseccion(a, b, tolerancia)

    print("=" * 62)
    if raiz is not None:
        print(f"  Raíz aproximada : y ≈ {raiz:.5f}")
        print(f"  f(raíz)         : {f(raiz):.5e}")
        print(f"  Iteraciones     : {num_iter}")
    print("=" * 62)
