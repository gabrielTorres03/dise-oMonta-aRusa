import unittest
import numpy as np
from montana_rusa import resolver_ecuaciones

class TestResolverEcuaciones(unittest.TestCase):

    def test_resolver_ecuaciones(self):
        A = np.array([[1, 2], [3, -1]])
        b = np.array([4, -2])
        resultado = resolver_ecuaciones(A, b)

        # Verificar que los resultados sean correctos
        self.assertAlmostEqual(resultado[0], 2)   # Primer incógnita
        self.assertAlmostEqual(resultado[1], -1)  # Segunda incógnita

if __name__ == '__main__':
    unittest.main()
