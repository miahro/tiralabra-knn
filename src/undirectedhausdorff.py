"""Tämä moduuli sisältää luokan suuntaamattomia Hausdorffin etäisyyksiä varten"""

#import numpy as np
#from math import sqrt, ceil
from directedhausdorff import DirectedHausdorff

class UndirectedHausdorff:
    """Luokka suuntaamattomia Hausdorffin etäisyyksiä varten
        Attributes: pistejoukot A ja B, pisteinä [x,y]
        kaavat esitetty paremmassa matemaattisessa muodossa
        erillisessä Kaavat.pdf dokumentissa
    """

    def __init__(self, A, B, d, altd6=False):
        """Luokan konstruktori, joka saa parametreinä piste-
            joukot A ja B, ja luo vastaavat
            suunnatut Hausdorffin etäisyys oliot
            Attributes: d = käytetty suunnatun etäisyyden funktio
            altd6 = False/True, vaihtoehtoinen kaava suunnatulle etäisyydelle d6
        """
        self.AB = DirectedHausdorff(A,B)
        self.BA = DirectedHausdorff(B,A) # pylint: disable=W1114
        self.d = d
        self.altd6 = altd6
        self.NA = len(A)
        self.NB = len(B)


#huomio, tämä if-elif-else hässäkkä ei ole kovin hyvää tekniikka, mutta
#oikean toiminnan takaamiseksi turvallinen tässä vaiheessa
#__call__ __callable__ tms käyttö lisää kohtuuttomasti virhemahdollisuutta
    def f1(self):
        """Palauttaa f1(A,B) suuntamattoman Hausdorffin etäisyyden
            eli min(d(A,B), d(B,A)) käyttäen suunnattuna etäisyytenä dn
            luokan attribuuttia d = 1,2,3,4,5,6
        """
        if self.d == 1:
            result = min(self.AB.d1(), self.BA.d1())
        elif self.d == 2:
            result = min(self.AB.d2(), self.BA.d2())
        elif self.d == 3:
            result = min(self.AB.d3(), self.BA.d3())
        elif self.d == 4:
            result = min(self.AB.d4(), self.BA.d4())
        elif self.d == 5:
            result = min(self.AB.d5(), self.BA.d5())
        elif self.d == 6:
            if not self.altd6:
                result = min(self.AB.d6(), self.BA.d6())
            else:
                result = min(self.AB.d6b(), self.BA.d6b())
        else:
            raise ValueError
        return result


    def f2(self):
        """Palauttaa f2(A,B) suuntamattoman Hausdorffin etäisyyden
            eli max(d(A,B), d(B,A)) käyttäen suunnattuna etäisyytenä dn
            luokan attribuuttia d = 1,2,3,4,5,6
        """
        if self.d == 1:
            result = max(self.AB.d1(), self.BA.d1())
        elif self.d == 2:
            result = max(self.AB.d2(), self.BA.d2())
        elif self.d == 3:
            result = max(self.AB.d3(), self.BA.d3())
        elif self.d == 4:
            result = max(self.AB.d4(), self.BA.d4())
        elif self.d == 5:
            result = max(self.AB.d5(), self.BA.d5())
        elif self.d == 6:
            if not self.altd6:
                result = max(self.AB.d6(), self.BA.d6())
            else:
                result = max(self.AB.d6b(), self.BA.d6b())
        else:
            raise ValueError
        return result


    def f3(self):
        """Palauttaa f3(A,B) suuntamattoman Hausdorffin etäisyyden
            eli keskiarvo(d(A,B), d(B,A)) käyttäen suunnattuna etäisyytenä dn
            luokan attribuuttia d = 1,2,3,4,5,6
        """
        if self.d == 1:
            result = (self.AB.d1() + self.BA.d1()) / 2
        elif self.d == 2:
            result = (self.AB.d2() + self.BA.d2()) / 2
        elif self.d == 3:
            result = (self.AB.d3() + self.BA.d3()) / 2
        elif self.d == 4:
            result = (self.AB.d4() + self.BA.d4()) / 2
        elif self.d == 5:
            result = (self.AB.d5() + self.BA.d5()) / 2
        elif self.d == 6:
            if not self.altd6:
                result = (self.AB.d6() + self.BA.d6()) / 2
            else:
                result = (self.AB.d6b() + self.BA.d6b()) / 2
        else:
            raise ValueError
        return result

    def f4(self):
        """Palauttaa f4(A,B) suuntamattoman Hausdorffin etäisyyden
            eli painotettu_keskiarvo(d(A,B), d(B,A)) käyttäen suunnattuna etäisyytenä dn
            luokan attribuuttia d = 1,2,3,4,5,6
        """
        if self.d == 1:
            result = (self.NA*self.AB.d1() + self.NB*self.BA.d1()) / (self.NA+self.NB)
        elif self.d == 2:
            result = (self.NA*self.AB.d2() + self.NB*self.BA.d2()) / (self.NA+self.NB)
        elif self.d == 3:
            result = (self.NA*self.AB.d3() + self.NB*self.BA.d3()) / (self.NA+self.NB)
        elif self.d == 4:
            result = (self.NA*self.AB.d4() + self.NB*self.BA.d4()) / (self.NA+self.NB)
        elif self.d == 5:
            result = (self.NA*self.AB.d5() + self.NB*self.BA.d5()) / (self.NA+self.NB)
        elif self.d == 6:
            if not self.altd6:
                result = (self.NA*self.AB.d6() + self.NB*self.BA.d6()) / (self.NA+self.NB)
            else:
                result = (self.NA*self.AB.d6b() + self.NB*self.BA.d6b()) / (self.NA+self.NB)
        else:
            raise ValueError
        return result
