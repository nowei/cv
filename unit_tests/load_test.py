import unittest
from PIL import Image
from ..load_image import *
class ConvolutionTest(unittest.TestCase):

    def setUp(self):
        self.path = './cv/unit_tests/fruits.png'
        self.im = Image.open(self.path)
        print("\ndone setting up")
    
    def testImageToRBGAArray(self):
        print('running testImageToRBGAArray')
        image, width, height, mode = imageToRBGAArray(self.path)
        im = RGBAArrayToImage(image, width, height, mode)
        orig = self.im.getdata()
        new = im.getdata()
        # print(len(orig))
        # for i in range(len(orig)):
            # if not (orig[i] == new[i]): print(orig[i], new[i])
        self.assertTrue(list(orig) == list(new))
        print('finished testImageToRBGAArray')

    def testImageToRGBAMultiDim(self):
        print('running testImageToRGBAMultiDim')
        image, width, height, mode = imageToRGBAMultiDim(self.path)
        im = RGBAMultiDimToImage(image, width, height, mode)
        orig = self.im.getdata()
        new = im.getdata()
        # print(len(orig))
        # for i in range(len(orig)):
            # if not (orig[i] == new[i]): print(orig[i], new[i])
        self.assertTrue(list(orig) == list(new))
        print('finished testImageToRGBAMultiDim')
    
    def testImageToRGBASingleArrs(self):
        print('running testImageToRGBASingleArrs')
        image, width, height, mode = imageToRGBASingleArrs(self.path)
        im = RGBASingleArrsToImage(image, width, height, mode)
        orig = self.im.getdata()
        new = im.getdata()
        self.assertTrue(list(orig) == list(new))
        print('finished testImageToRGBASingleArrs')

    def testImageToSingleArr(self):
        print('running testImageToSingleArr')
        image, width, height, mode = imageToSingleArr(self.path)
        im = singleArrToImage(image, width, height, mode)
        orig = self.im.getdata()
        new = im.getdata()
        # for i in range(len(orig)):
            # if not (orig[i] == new[i]): print(orig[i], new[i])
        self.assertTrue(list(orig) == list(new))
        # self.assertEqual(list(im.getdata()), list(self.im.getdata()))
        print('finished testImageToSingleArr')

    def testImageToRGBALists(self):
        print('running testImageToRGBALists')
        image, width, height, mode = imageToRGBALists(self.path)
        im = RGBAListToImage(image, width, height, mode)
        self.assertEqual(list(im.getdata()), list(self.im.getdata()))
        print('finished testImageToRGBALists')

if __name__ == '__main__':
    unittest.main()