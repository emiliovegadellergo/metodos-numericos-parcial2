import math

# Definición de la función f(x) = 5e^x - 2x - 10
def f(x):
    return 5 * math.exp(x) - 2 * x - 10

# Definición de la derivada f'(x) = 5e^x - 2
def df(x):
    return 5 * math.exp(x) - 2

def newton_raphson(x0, tolerancia=1e-5, max_iter=100):
    print(f"{'n':>4}  {'x_n':>12}  {'f(x_n)':>12}  {'Error rel.':>12}")
    print("-" * 48)

    x_actual = x0
    iteracion = 0

    # Primera fila: iteración 0 con el valor inicial (sin error relativo)
    fx = f(x_actual)
    print(f"{iteracion:>4}  {x_actual:>12.5f}  {fx:>12.5f}  {'---':>12}")

    while iteracion < max_iter:
        fx = f(x_actual)
        dfx = df(x_actual)

        # Evitar división por cero si la derivada es nula
        if dfx == 0:
            print("Derivada igual a cero. El método no puede continuar.")
            return None, iteracion

        # Fórmula de Newton-Raphson: x_{n+1} = x_n - f(x_n) / f'(x_n)
        x_nuevo = x_actual - fx / dfx

        # Cálculo del error relativo: |x_nuevo - x_actual| / |x_nuevo|
        if x_nuevo != 0:
            error_rel = abs(x_nuevo - x_actual) / abs(x_nuevo)
        else:
            error_rel = abs(x_nuevo - x_actual)

        iteracion += 1
        fx_nuevo = f(x_nuevo)
        print(f"{iteracion:>4}  {x_nuevo:>12.5f}  {fx_nuevo:>12.5f}  {error_rel:>12.5e}")

        # Verificar criterio de paro
        if error_rel < tolerancia:
            return x_nuevo, iteracion

        x_actual = x_nuevo

    print("Se alcanzó el máximo de iteraciones sin converger.")
    return x_actual, iteracion


if __name__ == "__main__":
    x0 = 0          # Valor inicial
    tolerancia = 1e-5

    print("=" * 48)
    print("  Método de Newton-Raphson")
    print("  f(x) = 5e^x - 2x - 10 = 0")
    print(f"  x0 = {x0},  tolerancia = {tolerancia}")
    print("=" * 48)

    raiz, num_iter = newton_raphson(x0, tolerancia)

    print("=" * 48)
    if raiz is not None:
        print(f"  Raíz encontrada : x ≈ {raiz:.5f}")
        print(f"  f(raíz)         : {f(raiz):.5e}")
        print(f"  Iteraciones     : {num_iter}")
    print("=" * 48)
