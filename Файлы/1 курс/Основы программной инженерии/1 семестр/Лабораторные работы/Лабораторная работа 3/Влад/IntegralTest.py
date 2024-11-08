import unittest
from Equations import cubic
from Equations import check
from Equations import predel_check

list_errorcoefs1 = ["Строка", True, 15, 1.2]
list_errorcoefs2 = [1, 2, 0, 4]
list_coefs = [1, 2, -1, -2]
list_answers = [1, -2, -1]


class TestEquations (unittest.TestCase):
    def test_1(self): #проверяем, подходят ли коэфф-ы для решения уравнения
        self.assertEqual(check(list_errorcoefs1), False)
        self.assertEqual(check(list_errorcoefs2), False)
        self.assertEqual(check(list_coefs), True)
    def test_2(self): #проверяем, правильно ли просчитываются корни
        self.assertEqual(cubic(list_coefs), list_answers)
    def test_3(self): #проверяем работу модуля проверки корней
        self.assertEqual(predel_check(list_coefs), True)
        
if __name__ == '__main__':
    unittest.main()