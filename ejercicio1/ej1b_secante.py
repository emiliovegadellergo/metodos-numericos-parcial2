import math

# Definición de la función f(x) = sqrt(x) - 2*ln(x)
def f(x):
    return math.sqrt(x) - 2 * math.log(x)

def secante(x0, x1, tolerancia=1e-5, max_iter=100):
    print(f"{'n':>4}  {'x_n':>12}  {'f(x_n)':>12}  {'Error rel.':>12}")
    print("-" * 48)

    # Mostrar los dos valores iniciales sin error relativo
    print(f"{0:>4}  {x0:>12.5f}  {f(x0):>12.5f}  {'---':>12}")
    print(f"{1:>4}  {x1:>12.5f}  {f(x1):>12.5f}  {'---':>12}")

    x_prev = x0
    x_actual = x1

    for iteracion in range(2, max_iter + 2):
        fx_prev = f(x_prev)
        fx_actual = f(x_actual)

        # Evitar división por cero si f(x_n) == f(x_{n-1})
        if fx_actual - fx_prev == 0:
            print("División por cero: f(x_n) = f(x_{n-1}). El método no puede continuar.")
            return None, iteracion - 2

        # Fórmula de la Secante:
        # x_{n+1} = x_n - f(x_n) * (x_n - x_{n-1}) / (f(x_n) - f(x_{n-1}))
        x_nuevo = x_actual - fx_actual * (x_actual - x_prev) / (fx_actual - fx_prev)

        # Verificar que x_nuevo esté en el dominio (x > 0 para sqrt y ln)
        if x_nuevo <= 0:
            print(f"Error en iteración {iteracion}: x_nuevo = {x_nuevo:.5f} ≤ 0.")
            print("El valor salió del dominio. Verifica los valores iniciales.")
            return None, iteracion - 2

        # Cálculo del error relativo: |x_nuevo - x_actual| / |x_nuevo|
        error_rel = abs(x_nuevo - x_actual) / abs(x_nuevo)

        fx_nuevo = f(x_nuevo)
        print(f"{iteracion:>4}  {x_nuevo:>12.5f}  {fx_nuevo:>12.5f}  {error_rel:>12.5e}")

        # Verificar criterio de paro
        if error_rel < tolerancia:
            return x_nuevo, iteracion - 1  # iteraciones efectivas desde n=1

        # Desplazar ventana: el actual se convierte en el previo
        x_prev = x_actual
        x_actual = x_nuevo

    print("Se alcanzó el máximo de iteraciones sin converger.")
    return x_actual, max_iter


if __name__ == "__main__":
    x0 = 3          # Primer valor inicial (cerca de la raíz ≈ 2.05)
    x1 = 5          # Segundo valor inicial
    tolerancia = 1e-5

    print("=" * 48)
    print("  Método de la Secante")
    print("  f(x) = sqrt(x) - 2*ln(x) = 0")
    print(f"  x0 = {x0},  x1 = {x1},  tolerancia = {tolerancia}")
    print("=" * 48)

    raiz, num_iter = secante(x0, x1, tolerancia)

    print("=" * 48)
    if raiz is not None:
        print(f"  Raíz encontrada : x ≈ {raiz:.5f}")
        print(f"  f(raíz)         : {f(raiz):.5e}")
        print(f"  Iteraciones     : {num_iter}")
    print("=" * 48)
