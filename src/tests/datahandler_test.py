"""yksikkötestit datahandler modulille"""
import unittest
from datahandler import DataHandler
from utils import square_dist_matrix, list_of_indices
from testcases import A, B, C, Am, Bm, Cm, A2, A2m, C2, C2m
from pathlib import Path
from config import OUTPUTFILEPATH


class TestDataHandler(unittest.TestCase):
    """yksikkötestit KNN luokalle"""

    def setUp(self):
        self.datahandler = DataHandler()
       #self.datahandler.read_mnist()

    def test_read_mnist(self):
        self.datahandler.read_mnist()
        self.assertEqual(len(self.datahandler.mnist.X_test), 10000)

    def test_set_filter(self):
        self.datahandler.set_filter(100)
        self.assertEqual(self.datahandler.filter_value, 100)

    def test_set_parameters(self):
        self.datahandler.set_parameters(10, 100, 20, 200, k=9, layers=6)
        self.assertEqual(self.datahandler.test_index_start, 10)
        self.assertEqual(self.datahandler.test_index_end, 100)
        self.assertEqual(self.datahandler.train_index_start, 20)
        self.assertEqual(self.datahandler.train_index_end, 200)
        self.assertEqual(self.datahandler.k, 9)
        self.assertEqual(self.datahandler.layers, 6)

    def test_init_knn(self):
        self.datahandler.read_mnist()
        self.datahandler.set_parameters(10, 100, 20, 200, k=9, layers=6)
        self.datahandler.init_knn()
        self.assertEqual(self.datahandler.knn.n, 90)
        self.assertEqual(self.datahandler.knn.m, 180)
        self.assertEqual(self.datahandler.knn.k, 9)
        self.assertEqual(self.datahandler.knn.layers, 6)

    def test_predict(self):
        self.datahandler.read_mnist()
        self.datahandler.set_parameters(0, 2, 0, 10, k=1, layers=1)
        self.datahandler.init_knn()
        self.datahandler.predict()
        self.assertEqual(len(self.datahandler.Y_predicted), 2)

    def test_evaluate_fail(self):
        self.datahandler.read_mnist()
        self.assertEqual(self.datahandler.evaluate(), {})

    def test_evaluate(self):
        self.datahandler.read_mnist()
        self.datahandler.set_parameters(0, 1, 0, 10, k=1, layers=1)
        self.datahandler.init_knn()
        self.datahandler.predict()
        self.assertEqual(len(self.datahandler.evaluate()), 15)

    def test_write_results_to_file(self):
        self.datahandler.read_mnist()          
        self.datahandler.write_results_to_file()
        self.assertEqual(Path(OUTPUTFILEPATH).is_file(), False)
        self.datahandler.set_parameters(0, 2, 0, 10, k=1, layers=1)
        self.datahandler.init_knn()
        self.datahandler.predict()
        self.datahandler.write_results_to_file()
        self.datahandler.write_results_to_file()
        self.assertEqual(Path(OUTPUTFILEPATH).is_file(), True)



