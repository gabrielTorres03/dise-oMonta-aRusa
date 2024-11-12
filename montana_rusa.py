#Inicio del ejercicio
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Datos para el trazador cúbico
x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([0.5, 0.8, 1.0, 0.9, 1.2, 0.7])

# Creacion del trazador cúbico
cs = CubicSpline(x_data, y_data)

# Valores para graficar la curva
x_vals = np.linspace(0, 5, 100)
y_vals = cs(x_vals)

# Grafica
plt.figure(figsize=(10, 5))
plt.plot(x_data, y_data, 'o', label='Puntos de Control')
plt.plot(x_vals, y_vals, label='Trazador Cúbico Sujeto')
plt.title('Método de Trazador Cúbico Sujeto')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()

# Datos para el Polinomio de Mínimos Cuadrados
x_data_poly = np.array([0, 1, 2, 3, 4])
y_data_poly = np.array([1.1, 3.5, 2.8, 4.2, 5.0])

# Ajustes de un polinomio de grado n (en este caso n=2)
coeffs = np.polyfit(x_data_poly, y_data_poly, deg=2)
poly_eq = np.poly1d(coeffs)

# Valores para graficar la curva ajustada
x_vals_poly = np.linspace(0, 4, 100)
y_vals_poly = poly_eq(x_vals_poly)

# Grafica
plt.figure(figsize=(10, 5))
plt.plot(x_data_poly, y_data_poly, 'o', label='Datos Experimentales')
plt.plot(x_vals_poly, y_vals_poly, label='Polinomio Ajustado')
plt.title('Ajuste de Polinomio por Mínimos Cuadrados')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
print("Coeficientes del polinomio ajustado:", coeffs)

from numpy.polynomial import Chebyshev

# Definición del polinomio de Chebyshev
cheb_coeffs = Chebyshev.fit(x_data_poly, y_data_poly, deg=3)

# Valores para graficar el polinomio de Chebyshev
x_vals_cheb = np.linspace(0, 4, 100)
y_vals_cheb = cheb_coeffs(x_vals_cheb)

# Grafica
plt.figure(figsize=(10, 5))
plt.plot(x_data_poly, y_data_poly, 'o', label='Datos Experimentales')
plt.plot(x_vals_cheb, y_vals_cheb, label='Polinomio de Chebyshev')
plt.title('Optimización con Polinomios Ortogonales')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()

# Datos para la Resolución de las Ecuaciones Lineales
A = np.array([[1, 2, 1], [2, -1, 1], [3, 1, -1]])
b = np.array([4, 1, -2])

# Resolución del sistema Ax = b
forces = np.linalg.solve(A, b)

print("Fuerzas en los puntos críticos:", forces)
# Programa Terminado
