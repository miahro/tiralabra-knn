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
        point_list = list_of_indices(square_dist_matrix(layers=3))
        self.knn = KNN([A], [Am], [1], [B], [Bm], point_list, k=1)
        self.knn_same = KNN([A], [Am], [1], [A], [Am], point_list, k=1)
        self.knn_close = KNN([A], [Am], [1], [C], [Cm], point_list, k=1)

    def test_Hausdorff_distance(self):
        """vertaa laskettua Hausdorffin etäisyyttä manuaalisesti laskettuun"""
        self.assertEqual(self.knn.hausdorff_distance(0,0), 39132)

    def test_hausdorff_same(self):
        """testaa, että knn.predict palauttaa oikean arvon oikeassa muodossa
        testitapauksessa vain yhden mittainen lista [1]"""
        self.assertEqual(self.knn_same.hausdorff_distance(0,0), 0)

    def test_hausdorff_close(self):
        """testaa, että knn.predict palauttaa oikean arvon oikeassa muodossa
        testitapauksessa vain yhden mittainen lista [1]"""
        self.assertEqual(self.knn_close.hausdorff_distance(0,0), 14682)


    def test_predict(self):
        """testaa, että knn.predict palauttaa oikean arvon oikeassa muodossa
        testitapauksessa vain yhden mittainen lista [1]"""
        self.assertEqual(self.knn.predict(), [1])

    def test_predict_same(self):
        """testaa, että knn.predict palauttaa oikean arvon oikeassa muodossa
        testitapauksessa vain yhden mittainen lista [1]"""
        self.assertEqual(self.knn_same.predict(), [1])

    def test_predict_close(self):
        """testaa, että knn.predict palauttaa oikean arvon oikeassa muodossa
        testitapauksessa vain yhden mittainen lista [1]"""
        self.assertEqual(self.knn_close.predict(), [1])


    def test_predict_close(self):
        """testaa, että knn.predict palauttaa oikean arvon oikeassa muodossa
        testitapauksessa vain yhden mittainen lista [1]"""
        self.assertEqual(self.knn_close.predict(), [1])

    def test_predict_same(self):
        """testaa, että knn.predict palauttaa oikean arvon oikeassa muodossa
        testitapauksessa vain yhden mittainen lista [1]"""
        self.assertEqual(self.knn_same.predict(), [1])


    def test_predict2(self):
        """testaa, että knn.predict palauttaa oikean arvon oikeassa muodossa
        testitapauksessa vain yhden mittainen lista [1]"""
        self.assertEqual(self.knn.predict2(), [1])

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

