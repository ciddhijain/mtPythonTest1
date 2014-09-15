__author__ = 'Ciddhi'

import unittest
from gestures import *

class TestGestures(unittest.TestCase):

    # to test rock and paper ordering
    def testRockPaperOne(self):
        self.assertEqual(Rock()>Paper(), False)

    # to test rock and paper ordering
    def testRockPaperTwo(self):
        self.assertEqual(Rock()<=Paper(), True)

    # to test paper and scissor ordering
    def testPaperScissorOne(self):
        self.assertEquals(Paper()<Scissor(), True)

    # to test paper and scissor ordering
    def testPaperScissorTwo(self):
        self.assertEqual(Scissor()==Paper(), False)

    # to test rock and scissor ordering
    def testRockScissorOne(self):
        self.assertEqual(Rock()>=Scissor(), True)

    # to test rock and scissor ordering
    def testRockScissorTwo(self):
        self.assertEqual(Scissor()>Rock(), False)

    # to test rock - rock ordering
    def testRockRock(self):
        self.assertEqual(Rock()>Rock(), False)

    # to test paper - paper ordering
    def testPaperPaper(self):
        self.assertEqual(Paper()==Paper(), True)

    # to test scissor - scissor ordering
    def testScissorScissor(self):
        self.assertEqual(Scissor()<=Scissor(), True)


if __name__ == '__main__':
    unittest.main()
