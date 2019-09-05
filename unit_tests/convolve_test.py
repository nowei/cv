import unittest
from ..convolve import convolution
from ..kernels import create_identity
from random import randint
import sys
class ConvolutionTest(unittest.TestCase):

    def setUp(self):
        self.id1 = create_identity(1)
        self.id2 = create_identity(2)
        print("\ndone setting up")
    
    def check_identity(self, t):
        self.assertEqual(t, convolution(self.id1, t))
        self.assertEqual(t, convolution(self.id2, t))

    def test1(self):
        print('running test1')
        t = [[402]]
        self.check_identity(t)
        print('finished test1')

    def test2(self):
        print('running test2')
        t = [[1,2],[3,4]]
        self.check_identity(t)
        print('finished test2')
    
    def test3(self):
        print('running test3')
        t = [[1,2,3],[4,5,6],[7,8,9]]
        self.check_identity(t)
        print('finished test3')

    def test4(self):
        print('running test4')
        t = [[randint(0, 1000) for _ in range(100)] for _ in range(50)]
        self.check_identity(t)
        print('finished test4')

    def test5(self):
        print('running test5')
        t = [[1,2,3,4,5,6,7]]
        self.check_identity(t)
        print('finished test5')

    def test6(self):
        print('running test6')
        t = [[1],[2],[3],[4],[5],[6],[7]]
        self.check_identity(t)
        print('finished test6')

    def test7(self):
        print('running test7')
        t = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8]]
        self.check_identity(t)
        print('finished test7')

if __name__ == '__main__':
    unittest.main()