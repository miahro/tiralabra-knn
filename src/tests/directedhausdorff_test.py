"""yksikkötestit directedhausdorff modulille"""
import unittest
from directedhausdorff import DirectedHausdorff
from testcases import A, B

class TestDirectedHausdorff(unittest.TestCase):
    """yksikkötestit suunnatun Hausdorffin etäisyyden funktioille d1-d6"""
    def setUp(self):
        """luodaan testi joukot python modulissa testcases määritellyistä joukoista
        A ja B. Luodaan joukot molemmin päin (A,B) ja (B,A)"""
        self.dhd_AB = DirectedHausdorff(A,B)
        self.dhd_BA = DirectedHausdorff(B,A) # pylint: disable=W1114

    def test_creation(self):
        """varmistetaan, että DirectedHausdorff olion pistejoukot A ja B vastaavat
        testcases pistejoukkoja, ts. myös järjestys toimii"""
        self.assertEqual((self.dhd_AB.A-A).all(), 0)
        self.assertEqual((self.dhd_AB.B-B).all(), 0)
        self.assertEqual((self.dhd_BA.A-B).all(), 0)
        self.assertEqual((self.dhd_BA.B-A).all(), 0)

    def test_d1(self):
        """testataan etäisyysfunktio d1 manuaalisesti laskutta arvoa vastaan"""
        self.assertAlmostEqual(self.dhd_AB.d1(), 28.2842712474619, places=13)
        self.assertAlmostEqual(self.dhd_BA.d1(), 28.2842712474619, places=13)


    def test_d2(self):
        """testataan etäisyysfunktio d2 manuaalisesti laskutta arvoa vastaan"""
        self.assertAlmostEqual(self.dhd_AB.d2(), 31.1448230047949, places=13)
        self.assertAlmostEqual(self.dhd_BA.d2(), 30.4138126514911, places=13)

    def test_d3(self):
        """testataan etäisyysfunktio d3 manuaalisesti laskutta arvoa vastaan"""
        self.assertAlmostEqual(self.dhd_AB.d3(), 31.8904374382039, places=13)
        self.assertAlmostEqual(self.dhd_BA.d3(), 31.1448230047949, places=13)

    def test_d4(self):
        """testataan etäisyysfunktio d4 manuaalisesti laskutta arvoa vastaan"""
        self.assertAlmostEqual(self.dhd_AB.d4(), 33.2415402771893, places=13)
        self.assertAlmostEqual(self.dhd_BA.d4(), 31.8276609256791, places=13)

    def test_d5(self):
        """testataan etäisyysfunktio d5 manuaalisesti laskutta arvoa vastaan"""
        self.assertAlmostEqual(self.dhd_AB.d5(), 33.9411254969543, places=13)
        self.assertAlmostEqual(self.dhd_BA.d5(), 32.5269119345812, places=13)

    def test_d6(self):
        """testataan etäisyysfunktio d6 manuaalisesti laskutta arvoa vastaan"""
        self.assertAlmostEqual(self.dhd_AB.d6(), 31.1448239141278, places=13)
        self.assertAlmostEqual(self.dhd_BA.d6(), 30.4261398208627, places=13)

    def test_d6b(self):
        """testataan etäisyysfunktio d6b manuaalisesti laskutta arvoa vastaan"""
        self.assertAlmostEqual(self.dhd_AB.d6b(), 778.620597853196, places=13)
        self.assertAlmostEqual(self.dhd_BA.d6b(), 486.818237133803, places=13)
