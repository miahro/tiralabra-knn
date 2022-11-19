"""yksikkötestit KNN modulille"""
import unittest
from KNN import KNN
from testcases import A, B, Am, Bm

class TestKNN(unittest.TestCase):
    """yksikkötestit KNN luokalle"""
    def setUp(self):
        """luodaan testi joukot python modulissa testcases määritellyistä joukoista
        A ja B."""
        self.knn = KNN([A], [Am], [1], [B], [Bm], k=1)

    def test_Hausdorff_distance(self):
        """vertaa laskettua Hausdorffin etäisyyttä manuaalisesti laskettuun"""
        self.assertAlmostEqual(self.knn.hausdorff_distance(0,0), 1265.438834987, places=11)
        #pyöristysvirhe 11:sta merkitsevässä numerossa hyväksytään

    def test_predict(self):
        """testaa, että knn.predict palauttaa oikean arvon oikeassa muodossa
        testitapauksessa vain yhden mittainen lista [1]"""
        self.assertEqual(self.knn.predict(), [1])

    def test_predict2(self):
        """testaa, että knn.predict palauttaa oikean arvon oikeassa muodossa
        testitapauksessa vain yhden mittainen lista [1]"""
        self.assertEqual(self.knn.predict2(), [1])

