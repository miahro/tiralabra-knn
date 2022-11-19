"""yksikkötestit read_mnist modulille"""
import unittest
from mnistdata import Mnistdata

class TestMnistdata(unittest.TestCase):
    """yksikkötestit Mnistdata luokan luku
    ja konversiotoimille"""
    def setUp(self):
        """luodaan mnistwardata olio lukemalla tietokanta
        filteriarvona tässä mielivaltainen 115"""
        self.mndata = Mnistdata(filter_value=115)

    def test_X_train_matrix(self):
        """testataan, että X_train_matrix palauttaa oikean kokoisen listan
        oikean kokoisia matriiseja"""
        self.assertEqual(len(self.mndata.X_train_matrix()), 60000)
        self.assertEqual(len(self.mndata.X_train_matrix(start=0, end=5000)), 5000)
        for i in range(100):
            self.assertEqual(self.mndata.X_train_matrix(start=0, end=100)[i].shape, (28,28))


    def test_X_train_point_list(self):
        """testataan, että pistelista esitysmuoto on oikean muotoinen"""
        self.assertEqual(len(self.mndata.X_train_list(0, 5000)), 5000)
        self.assertEqual(len(self.mndata.X_train_list()), 60000)

    def test_X_test_matrix(self):
        """testataan, että X_train_matrix palauttaa oikean kokoisen listan 
        oikeankokosia matriiseja"""
        self.assertEqual(len(self.mndata.X_test_matrix()), 10000)
        self.assertEqual(len(self.mndata.X_test_matrix(start=0, end=5000)), 5000)
        for i in range(100):
            self.assertEqual(self.mndata.X_test_matrix(start=0, end=100)[i].shape, (28,28))


    def test_X_test_point_list(self):
        """testataan, että pistelista esitysmuoto on oikean muotoinen"""
        self.assertEqual(len(self.mndata.X_test_list(0, 5000)), 5000)
        self.assertEqual(len(self.mndata.X_test_list()), 10000)

    def test_Y_train_labels(self):
        """testataan, että Y_train_labels palauttaa oikean pituisen listan"""
        self.assertEqual(len(self.mndata.Y_train_labels()), 60000)
        self.assertEqual(len(self.mndata.Y_train_labels(start=0, end=5000)), 5000)

    def test_Y_test_labels(self):
        """testataan, että Y_test_labels palauttaa oikean pituisen listan"""
        self.assertEqual(len(self.mndata.Y_test_labels()), 10000)
        self.assertEqual(len(self.mndata.Y_test_labels(start=0, end=5000)), 5000)


    def test_read_Y_train_labels_range(self):
        """testataan, että testi_Y arvot ovat välillä 0-9"""
        Y = self.mndata.Y_train_labels(start=500, end=1000)
        for y in Y:
            self.assertTrue(0 <= y <= 9)


    def test_read_Y_test_labels_range(self):
        """testataan, että testi_Y arvot ovat välillä 0-9"""
        Y = self.mndata.Y_train_labels(start=500, end=1000)
        for y in Y:
            self.assertTrue(0 <= y <= 9)


    def test_read_X_train_list_range(self):
        """testataan, että training_X xy-arvot ovat välillä 0-27 """
        L = self.mndata.X_train_list(start=500, end=1000)
        for X in L:
            for x in X:
                self.assertTrue(0 <= x[0] <= 27)
                self.assertTrue(0 <= x[1] <= 27)

    def test_read_X_test_list_range(self):
        """testataan, että training_X xy-arvot ovat välillä 0-27 """
        L = self.mndata.X_test_list(start=500, end=1000)
        for X in L:
            for x in X:
                self.assertTrue(0 <= x[0] <= 27)
                self.assertTrue(0 <= x[1] <= 27)


