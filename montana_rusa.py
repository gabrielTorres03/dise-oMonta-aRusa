import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import CubicSpline
from numpy.polynomial import Chebyshev


# Función para el Trazador Cúbico
def trazador_cubico(x_data, y_data):
    cs = CubicSpline(x_data, y_data)
    x_vals = np.linspace(0, 5, 100)
    y_vals = cs(x_vals)

    plt.figure(figsize=(10, 5))
    plt.plot(x_data, y_data, 'o', label='Puntos de Control')
    plt.plot(x_vals, y_vals, label='Trazador Cúbico Sujeto')
    plt.title('Método de Trazador Cúbico Sujeto')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()
    plt.show()

    return cs


# Función para el Polinomio de Mínimos Cuadrados
def polinomio_minimos_cuadrados(x_data, y_data):
    coeffs = np.polyfit(x_data, y_data, deg=2)
    poly_eq = np.poly1d(coeffs)
    x_vals_poly = np.linspace(0, 4, 100)
    y_vals_poly = poly_eq(x_vals_poly)

    plt.figure(figsize=(10, 5))
    plt.plot(x_data, y_data, 'o', label='Datos Experimentales')
    plt.plot(x_vals_poly, y_vals_poly, label='Polinomio Ajustado')
    plt.title('Ajuste de Polinomio por Mínimos Cuadrados')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()
    plt.show()

    return coeffs


# Función para el Polinomio de Chebyshev
def polinomio_chebyshev(x_data, y_data):
    cheb_coeffs = Chebyshev.fit(x_data, y_data, deg=3)
    x_vals_cheb = np.linspace(0, 4, 100)
    y_vals_cheb = cheb_coeffs(x_vals_cheb)

    plt.figure(figsize=(10, 5))
    plt.plot(x_data, y_data, 'o', label='Datos Experimentales')
    plt.plot(x_vals_cheb, y_vals_cheb, label='Polinomio de Chebyshev')
    plt.title('Optimización con Polinomios Ortogonales')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()
    plt.show()

    return cheb_coeffs


# Función para resolver el sistema de ecuaciones
def resolver_ecuaciones(A, b):
    forces = np.linalg.solve(A, b)
    return forces


# Función principal que organiza todo
def main():
    # Datos para el trazador cúbico
    df = pd.read_csv("data_cubic.csv")
    x_data = df['x_data'].values
    y_data = df['y_data'].values

    # Llamar a la función trazador_cubico
    cs = trazador_cubico(x_data, y_data)

    # Datos para el Polinomio de Mínimos Cuadrados
    datos = pd.read_csv("data_poly.csv")
    x_data_poly = datos['x_data'].values
    y_data_poly = datos['y_data'].values

    # Llamar a la función polinomio_minimos_cuadrados
    coeffs = polinomio_minimos_cuadrados(x_data_poly, y_data_poly)
    print("Coeficientes del polinomio ajustado:", coeffs)

    # Llamar a la función polinomio_chebyshev
    cheb_coeffs = polinomio_chebyshev(x_data_poly, y_data_poly)

    # Datos para la Resolución de las Ecuaciones Lineales
    A = np.array([[1, 2, 1], [2, -1, 1], [3, 1, -1]])
    b = np.array([4, 1, -2])

    # Llamar a la función resolver_ecuaciones
    forces = resolver_ecuaciones(A, b)
    print("Fuerzas en los puntos críticos:", forces)


# Ejecutar el programa principal
if __name__ == '__main__':
    main()
