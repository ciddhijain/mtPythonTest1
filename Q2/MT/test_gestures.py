__author__ = 'Ciddhi'

import unittest
from gestures import *

class TestGestures(unittest.TestCase):

    def setUp(self):
        pass

    def testRockPaperOne(self):
        self.assertEqual(Rock()>Paper(), False)

    def testRockPaperTwo(self):
        self.assertEqual(Rock()<=Paper(), True)

    def testPaperScissorOne(self):
        self.assertEquals(Paper()<Scissor(), True)

    def testPaperScissorTwo(self):
        self.assertEqual(Scissor()==Paper(), False)

    def testRockScissorOne(self):
        self.assertEqual(Rock()>=Scissor(), True)

    def testRockScissorTwo(self):
        self.assertEqual(Scissor()>Rock(), False)

    def testRockRock(self):
        self.assertEqual(Rock()>Rock(), False)

    def testPaperPaper(self):
        self.assertEqual(Paper()==Paper(), True)

    def testScissorScissor(self):
        self.assertEqual(Scissor()<=Scissor(), True)


if __name__ == '__main__':
    unittest.main()
