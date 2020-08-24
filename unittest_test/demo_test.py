# -*- coding:utf-8 -*-
import unittest


class Demo1Test(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_demo_1(self):
        self.assertEqual(1, 2)

    def test_demo_2(self):
        self.assertEqual(1, 1)


class Demo2Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_demo_1(self):
        self.assertEqual(1, 2)

    def test_demo_2(self):
        self.assertEqual(1, 1)


suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Demo1Test))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Demo2Test))
