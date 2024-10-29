import unittest
from Cube import cubic

mass1_1 = [3,-4,-3]
mass1_2 = [1,-2,-1]

mass2_1 = [0,1,35,3]
mass2_2 = [5,0,2,1]
mass2_3 = [5,2,0,1]
mass2_4 = [5,2,2,0]
class TestCube(unittest.TestCase):
    
    def test_cubic(self):
        self.assertEqual(cubic(1,4,-9,-36),mass1_1) #Сравнение решения при обычных цифрах
        self.assertEqual(cubic(1,2,-1,-2),mass1_2)
        
    def test_cubic2(self):
        self.assertRaises(ValueError, cubic, mass2_1)
    
    # def test_cubic3(self):
    #     self.assertRaises()

if __name__ == '__main__':
    unittest.main()