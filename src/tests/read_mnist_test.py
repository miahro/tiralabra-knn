"""yksikkötestit read_mnist modulille"""
import unittest
from read_mnist import Mnistrawdata

class TestMnistrawdata(unittest.TestCase):
    """yksikkötestit suunnatun Mnistrawdata luku
    ja konversiotoimille"""
    def setUp(self):
        """luodaan mnistwardata olio lukemalla tietokanta
        filteriarvona tässä mielivaltainen 115"""
        self.mnraw = Mnistrawdata(filter_value=115)

    def test_read_training_x(self):
        """testataan, että read_training_x palauttaa oikean määrän pisteitä"""
        self.assertEqual(len(self.mnraw.read_training_x(0, 5000)), 5000)
        self.assertEqual(len(self.mnraw.read_training_x()), 60000)

    def test_read_training_y(self):
        """testataan, että read_training_y palauttaa oikean määrän pisteitä"""
        self.assertEqual(len(self.mnraw.read_training_y(0, 5000)), 5000)
        self.assertEqual(len(self.mnraw.read_training_y()), 60000)

    def test_read_testing_x(self):
        """testataan, että read_testing_x palauttaa oikean määrän pisteitä"""
        self.assertEqual(len(self.mnraw.read_testing_x(0, 5000)), 5000)
        self.assertEqual(len(self.mnraw.read_testing_x()), 10000)

    def test_read_testing_y(self):
        """testataan, että read_training_y palauttaa oikean määrän pisteitä"""
        self.assertEqual(len(self.mnraw.read_testing_y(0, 5000)), 5000)
        self.assertEqual(len(self.mnraw.read_testing_y()), 10000)

    def test_read_testing_y_datarange(self):
        """testataan, että testi_Y arvot ovat välillä 0-9"""
        Y = self.mnraw.read_testing_y()
        for y in Y:
            self.assertTrue(0 <= y <= 9)

    def test_read_training_y_datarange(self):
        """testataan, että testi_Y arvot ovat välillä 0-9"""
        Y = self.mnraw.read_training_y()
        for y in Y:
            self.assertTrue(0 <= y <= 9)

    def test_read_training_x_datarange(self):
        """testataan, että training_X xy-arvot ovat välillä 0-27 """
        L = self.mnraw.read_training_x()
        for X in L:
            for x in X:
                self.assertTrue(0 <= x[0] <= 27)
                self.assertTrue(0 <= x[1] <= 27)

    def test_read_testing_x_datarange(self):
        """testataan, että testing_X xy-arvot ovat välillä 0-27 """
        L = self.mnraw.read_testing_x()
        for X in L:
            for x in X:
                self.assertTrue(0 <= x[0] <= 27)
                self.assertTrue(0 <= x[1] <= 27)
