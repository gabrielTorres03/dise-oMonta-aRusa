import unittest
import numpy as np
from montana_rusa import polinomio_minimos_cuadrados

class TestPolinomioMinimosCuadrados(unittest.TestCase):

    def test_polinomio_minimos_cuadrados(self):
        x_data = np.array([0, 1, 2])
        y_data = np.array([1.0, 2.0, 3.0])
        coeffs = polinomio_minimos_cuadrados(x_data, y_data)

        # Verificar que los coeficientes sean correctos (en este caso debería ser un polinomio lineal)
        self.assertAlmostEqual(coeffs[0], 1)  # Coeficiente de x
        self.assertAlmostEqual(coeffs[1], 1)  # Coeficiente constante

if __name__ == '__main__':
    unittest.main()
