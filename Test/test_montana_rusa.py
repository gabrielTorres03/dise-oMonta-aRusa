import unittest
import numpy as np
from montana_rusa import trazador_cubico, polinomio_minimos_cuadrados, resolver_ecuaciones

class TestMontanaRusa(unittest.TestCase):

    def test_trazador_cubico(self):
        x_data = np.array([0, 1, 2])
        y_data = np.array([0.5, 0.8, 1.0])
        cs = trazador_cubico(x_data, y_data)

        # Verificar que el valor interpolado en x=1.5 esté dentro del rango esperado
        interpolado = cs(1.5)
        self.assertGreaterEqual(interpolado, min(y_data))
        self.assertLessEqual(interpolado, max(y_data))

    def test_polinomio_minimos_cuadrados(self):
        x_data = np.array([0, 1, 2])
        y_data = np.array([1.0, 2.0, 3.0])
        coeffs = polinomio_minimos_cuadrados(x_data, y_data)

        # Verificar que los coeficientes sean correctos (en este caso debería ser un polinomio lineal)
        self.assertAlmostEqual(coeffs[0], 1)  # Coeficiente de x
        self.assertAlmostEqual(coeffs[1], 1)  # Coeficiente constante

    def test_resolver_ecuaciones(self):
        A = np.array([[1, 2], [3, -1]])
        b = np.array([4, -2])
        resultado = resolver_ecuaciones(A, b)

        # Verificar que los resultados sean correctos
        self.assertAlmostEqual(resultado[0], 2)   # Primer incógnita
        self.assertAlmostEqual(resultado[1], -1)  # Segunda incógnita

if __name__ == '__main__':
    unittest.main()
    