"""Tämä moduuli sisältää luokan suunnattuja Hausdorffin etäisyyksiä varten"""

#import numpy as np
from math import sqrt, ceil

class DirectedHausdorff:
    """Luokka suunnattuja Hausdorffin etäisyyksiä varten
        Attributes: pistejoukot A ja B, pisteinä [x,y]
        kaavat esitetty paremmassa matemaattisessa muodossa
        erillisessä Kaavat.pdf dokumentissa
    """

    def __init__(self, A, B):
        """Luokan konstruktori, joka saa parametreinä piste-
            joukot A ja B
        """
        self.A = A
        self.B = B

    @staticmethod
    def euclidean(a, b):
        """pisteiden a ja b [x,y] välinen
            normaali euklidinen etäisyys
        """
        return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

    def dist_point_set(self, a):
        """Pisteen ja pistejoukon välinen etäisyys
        piste a parametrina, pistejoukko B luokan attribuutti
        """
        result = [self.euclidean(a,b) for b in self.B]
        result.sort()
        return result[0]

    def dist_set_set(self):
        """Apufunktio, joka joka laskee pistejoukon A kaikkien pisteiden
        etäisyyden pistejoukkoon B. Etäisyydet palautetaan järjestettynä listana
        """
        result = [self.dist_point_set(a) for a in self.A]
        result.sort()
        return result

    def d1(self):
        """d1(A,B) palauttaa minimin"""
        return self.dist_set_set()[0]

    def d2(self):
        """d2(A,B) palauttaa 50%:n järjestetyn etäisyyden
        """
        return self.dist_set_set()[ceil(0.5*len(self.A))-1]

    def d3(self):
        """d3(A,B) palauttaa 75%:n järjestetyn etäisyyden
        """
        return self.dist_set_set()[ceil(0.75*len(self.A))-1]

    def d4(self):
        """d4(A,B) palauttaa 90%:n järjestetyn etäisyyden
        """
        return self.dist_set_set()[ceil(0.9*len(self.A))-1]

    def d5(self):
        """d5(A,B) palauttaa maksimietäisyyden
        """
        return self.dist_set_set()[-1]

    def d6(self):
        """d6(A,B) palauttaa etäisyyksien keskiarvon
        """
        return sum(self.dist_set_set())/len(self.A)

    def d6b(self):
        """d6(A,B) palauttaa etäisyyksien summan
        """
        return sum(self.dist_set_set())
