import math

# Definición de la función f(t) = cos(t) - e^(-t)
def f(t):
    return math.cos(t) - math.exp(-t)

# Definición de la derivada f'(t) = -sin(t) + e^(-t)
def df(t):
    return -math.sin(t) + math.exp(-t)

def newton_raphson(t0, tolerancia=1e-5, max_iter=100):
    print(f"{'n':>4}  {'t_n':>12}  {'f(t_n)':>12}  {'Error rel.':>12}")
    print("-" * 48)

    t_actual = t0
    iteracion = 0

    # Fila inicial: valor de arranque sin error relativo
    print(f"{iteracion:>4}  {t_actual:>12.5f}  {f(t_actual):>12.5f}  {'---':>12}")

    while iteracion < max_iter:
        ft = f(t_actual)
        dft = df(t_actual)

        # Evitar división por cero si la derivada es nula
        if dft == 0:
            print("Derivada igual a cero. El método no puede continuar.")
            return None, iteracion

        # Fórmula de Newton-Raphson: t_{n+1} = t_n - f(t_n) / f'(t_n)
        t_nuevo = t_actual - ft / dft

        # Cálculo del error relativo: |t_nuevo - t_actual| / |t_nuevo|
        if t_nuevo != 0:
            error_rel = abs(t_nuevo - t_actual) / abs(t_nuevo)
        else:
            error_rel = abs(t_nuevo - t_actual)

        iteracion += 1
        print(f"{iteracion:>4}  {t_nuevo:>12.5f}  {f(t_nuevo):>12.5f}  {error_rel:>12.5e}")

        # Verificar criterio de paro
        if error_rel < tolerancia:
            return t_nuevo, iteracion

        t_actual = t_nuevo

    print("Se alcanzó el máximo de iteraciones sin converger.")
    return t_actual, iteracion


if __name__ == "__main__":
    t0 = 1          # Valor inicial
    tolerancia = 1e-5

    print("=" * 48)
    print("  Método de Newton-Raphson")
    print("  f(t) = cos(t) - e^(-t) = 0")
    print(f"  t0 = {t0},  tolerancia = {tolerancia}")
    print("=" * 48)

    raiz, num_iter = newton_raphson(t0, tolerancia)

    print("=" * 48)
    if raiz is not None:
        print(f"  Raíz encontrada : t ≈ {raiz:.5f}")
        print(f"  f(raíz)         : {f(raiz):.5e}")
        print(f"  Iteraciones     : {num_iter}")
    print("=" * 48)
