"""yksikkötesti undirectedhausdorff modulille"""
import unittest
from undirectedhausdorff import UndirectedHausdorff
from testcases import A, B

class TestUndirectedHausdorff(unittest.TestCase): # pylint: disable=R0902
    """yksikkötestit suuntaamattoman Hausdorffin etäisyyden funktioille f1-f4"""
    def setUp(self):
        """luondaan UndirectedHausdorff oliot testipistejoukoista A ja B
        oliot erikseen suunnatun Hausdorffin funktioilla d1-d6 sekä d6b
        d7 on virhetapauksen testiä varten"""
        self.udhd_AB1 = UndirectedHausdorff(A,B, d=1)
        self.udhd_AB2 = UndirectedHausdorff(A,B, d=2)
        self.udhd_AB3 = UndirectedHausdorff(A,B, d=3)
        self.udhd_AB4 = UndirectedHausdorff(A,B, d=4)
        self.udhd_AB5 = UndirectedHausdorff(A,B, d=5)
        self.udhd_AB6 = UndirectedHausdorff(A,B, d=6)
        self.udhd_AB6_alt = UndirectedHausdorff(A,B, d=6, altd6=True)
        self.udhd_AB7 = UndirectedHausdorff(A,B, d=7)

    def test_creation(self):
        """testataan jokaisen testiolion NA ja NB
        testijoukkojen pituuksia vastaan"""
        self.assertEqual(self.udhd_AB1.NA, len(A))
        self.assertEqual(self.udhd_AB1.NB, len(B))
        self.assertEqual(self.udhd_AB2.NA, len(A))
        self.assertEqual(self.udhd_AB2.NB, len(B))
        self.assertEqual(self.udhd_AB3.NA, len(A))
        self.assertEqual(self.udhd_AB3.NB, len(B))
        self.assertEqual(self.udhd_AB4.NA, len(A))
        self.assertEqual(self.udhd_AB4.NB, len(B))
        self.assertEqual(self.udhd_AB5.NA, len(A))
        self.assertEqual(self.udhd_AB5.NB, len(B))
        self.assertEqual(self.udhd_AB6.NA, len(A))
        self.assertEqual(self.udhd_AB6.NB, len(B))
        self.assertEqual(self.udhd_AB6_alt.NA, len(A))
        self.assertEqual(self.udhd_AB6_alt.NB, len(B))

    def test_value_error(self):
        """varmistetaan, että suunnatun Hausdorffin etäisyyden kutsuminen suuremmalla
        kuin arvolla d=6 aiheuttaa virheen"""
        with self.assertRaises(ValueError):
            self.udhd_AB7.f1()
        with self.assertRaises(ValueError):
            self.udhd_AB7.f2()
        with self.assertRaises(ValueError):
            self.udhd_AB7.f3()
        with self.assertRaises(ValueError):
            self.udhd_AB7.f4()


    def test_f1(self):
        """suuntamaattoman Hausdorffin etäisyyden funktion f1 testaus
        suunnatun etäisyyden funktioilla d1-d6 ja d6b"""
        self.assertAlmostEqual(self.udhd_AB1.f1(), 28.2842712474619, places=13)
        self.assertAlmostEqual(self.udhd_AB2.f1(), 30.4138126514911, places=13)
        self.assertAlmostEqual(self.udhd_AB3.f1(), 31.1448230047949, places=13)
        self.assertAlmostEqual(self.udhd_AB4.f1(), 31.8276609256791, places=13)
        self.assertAlmostEqual(self.udhd_AB5.f1(), 32.5269119345812, places=13)
        self.assertAlmostEqual(self.udhd_AB6.f1(), 30.4261398208627, places=13)
        self.assertAlmostEqual(self.udhd_AB6_alt.f1(), 486.818237133803, places=13)

    def test_f2(self):
        """suuntamaattoman Hausdorffin etäisyyden funktion f2 testaus
        suunnatun etäisyyden funktioilla d1-d6 ja d6b"""
        self.assertAlmostEqual(self.udhd_AB1.f2(), 28.2842712474619, places=13)
        self.assertAlmostEqual(self.udhd_AB2.f2(), 31.1448230047949, places=13)
        self.assertAlmostEqual(self.udhd_AB3.f2(), 31.8904374382039, places=13)
        self.assertAlmostEqual(self.udhd_AB4.f2(), 33.2415402771893, places=13)
        self.assertAlmostEqual(self.udhd_AB5.f2(), 33.9411254969543, places=13)
        self.assertAlmostEqual(self.udhd_AB6.f2(), 31.1448239141278, places=13)
        self.assertAlmostEqual(self.udhd_AB6_alt.f2(), 778.620597853196, places=13)

    def test_f3(self):
        """suuntamaattoman Hausdorffin etäisyyden funktion f3 testaus
        suunnatun etäisyyden funktioilla d1-d6 ja d6b"""
        self.assertAlmostEqual(self.udhd_AB1.f3(), 28.2842712474619, places=13)
        self.assertAlmostEqual(self.udhd_AB2.f3(), 30.779317828143, places=13)
        self.assertAlmostEqual(self.udhd_AB3.f3(), 31.5176302214994, places=13)
        self.assertAlmostEqual(self.udhd_AB4.f3(), 32.5346006014342, places=13)
        self.assertAlmostEqual(self.udhd_AB5.f3(), 33.2340187157677, places=13)
        self.assertAlmostEqual(self.udhd_AB6.f3(), 30.7854818674953, places=13)
        self.assertAlmostEqual(self.udhd_AB6_alt.f3(), 632.7194174935, places=12)
        #viimeisessä testissä tulee pyöristysvirhe 13:sta merkitsevässä numerossa,
        #kuitenkin selvästi vain pyöristysvirhe, joten testikriteeriä säädetty

    def test_f4(self):
        """suuntamaattoman Hausdorffin etäisyyden funktion f4 testaus
        suunnatun etäisyyden funktioilla d1-d6 ja d6b"""
        self.assertAlmostEqual(self.udhd_AB1.f4(), 28.2842712474619, places=13)
        self.assertAlmostEqual(self.udhd_AB2.f4(), 30.8595506717983, places=13)
        self.assertAlmostEqual(self.udhd_AB3.f4(), 31.5994659519955, places=13)
        self.assertAlmostEqual(self.udhd_AB4.f4(), 32.689782481478, places=13)
        self.assertAlmostEqual(self.udhd_AB5.f4(), 33.3892372774916, places=13)
        self.assertAlmostEqual(self.udhd_AB6.f4(), 30.8643618289512, places=13)
        self.assertAlmostEqual(self.udhd_AB6_alt.f4(), 664.74650586514, places=12)
        #viimeisessä testissä tulee pyöristysvirhe 13:sta merkitsevässä numerossa,
        #kuitenkin selvästi vain pyöristysvirhe, joten testikriteeriä säädetty
