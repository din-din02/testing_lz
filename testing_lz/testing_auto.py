import unittest
from func import func 

class Test(unittest.TestCase):

    def test_integers(self):
        # Позитивный тест (целые числа)
        self.assertAlmostEqual(func(2, 3, 5, 3, 4), 4.5)

    def test_floats(self):
        #Позитивный тест (дробные числа)
        self.assertAlmostEqual(func(1.5, 2.5, 4.0, 2.0, 0.25), 2.5)

    def test_zero(self):
        # Тест: подкоренное выражение f равно нулю
        self.assertAlmostEqual(func(1, 1, 3, 1, 0), 1.0)

    def test_zerodivisionerror(self):
        #Тестирование ZeroDivisionError (c - d = 0)
        with self.assertRaises(ZeroDivisionError):
            func(5, 5, 2, 2, 9)

    def test_valueerror(self):
        #Тестирование ValueError (отрицательное под корнем)
        with self.assertRaises(ValueError):
            func(4, 2, 5, 1, -4)

    def test_typeerror(self):
        #Тестирование TypeError (строка вместо числа)
        with self.assertRaises(TypeError):
            func('2', 3, 5, 3, 4)

    def test_complex(self):
        #Тестирование TypeError (комплексное число)
        with self.assertRaises(TypeError):
            func(2, 3, 5, 3, complex(4, 1))

if __name__ == '__main__':
    unittest.main()
