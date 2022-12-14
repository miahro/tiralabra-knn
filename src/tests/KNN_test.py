"""yksikkötestit KNN modulille"""
import unittest
from KNN import KNN
from utils import square_dist_matrix, list_of_indices
from testcases import A, B, C, Am, Bm, Cm, A2, A2m, C2, C2m


class TestKNN(unittest.TestCase):
    """yksikkötestit KNN luokalle"""

    def setUp(self):
        """luodaan testi joukot python modulissa testcases määritellyistä joukoista
        A ja B."""
        self.knn = KNN([A], [Am], [1], [B], [Bm], k=1)
        self.knn_same = KNN([A], [Am], [1], [A], [Am], k=1)
        self.knn_close = KNN([A], [Am], [1], [C], [Cm], k=1)

    def test_predict3(self):
        """testaa, että knn.predict palauttaa oikean arvon oikeassa muodossa
        testitapauksessa vain yhden mittainen lista [1]"""
        self.assertEqual(self.knn.predict3(), [1])

    def test_predict3_same(self):
        """testaa, että knn.predict palauttaa oikean arvon oikeassa muodossa
        testitapauksessa vain yhden mittainen lista [1]"""
        self.assertEqual(self.knn_same.predict3(), [1])

    def test_predict3_close(self):
        """testaa, että knn.predict palauttaa oikean arvon oikeassa muodossa
        testitapauksessa vain yhden mittainen lista [1]"""
        self.assertEqual(self.knn_close.predict3(), [1])
