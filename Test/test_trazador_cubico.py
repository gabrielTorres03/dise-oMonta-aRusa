import unittest
import numpy as np
from montana_rusa import trazador_cubico

class TestTrazadorCubico(unittest.TestCase):

    def test_trazador_cubico(self):
        x_data = np.array([0, 1, 2])
        y_data = np.array([0.5, 0.8, 1.0])
        cs = trazador_cubico(x_data, y_data)

        # Verificar que el valor interpolado en x=1.5 esté dentro del rango esperado
        interpolado = cs(1.5)
        self.assertGreaterEqual(interpolado, min(y_data))
        self.assertLessEqual(interpolado, max(y_data))

if __name__ == '__main__':
    unittest.main()
