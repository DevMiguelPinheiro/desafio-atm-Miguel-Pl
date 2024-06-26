import unittest
from API.CaixaEletronico import CaixaEletronico

class TestCaixaEletronico(unittest.TestCase):
    def setUp(self):
        self.caixa = CaixaEletronico()

    def test_calculo_cedulas(self):
        self.assertEqual(self.caixa.calcular_cedulas(380), {100: 3, 50: 1, 20: 1, 10: 1, 5: 0, 2: 0})
        self.assertEqual(self.caixa.calcular_cedulas(122), {100: 1, 50: 0, 20: 1, 10: 0, 5: 0, 2: 1})
        self.assertEqual(self.caixa.calcular_cedulas(3), {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 1})

    def test_valor_invalido(self):
        with self.assertRaises(ValueError):
            self.caixa.calcular_cedulas(-10)
        with self.assertRaises(ValueError):
            self.caixa.calcular_cedulas(0)
        with self.assertRaises(ValueError):
            self.caixa.calcular_cedulas(1)

if __name__ == '__main__':
    unittest.main()
