"""moduli KNN luokkaa varten"""

from heapq import heappush, heappop
from collections import Counter
from arrays import SDM, PL


class KNN:
    """"K:n lähimmän naapurin luokka sisältää myös funktion Hausdorffin etäisyyden laskemiseksi
        Attributes:
            k: knn:n k eli montako lähintä naapuria huomioidaan
            X_train_points: opetusdata listana pistelistoja
            X_train_matrix: opetusdata listana matriiseja
            Y_train: opetusdatan ominaisuudet listana
            X_test_points: testidata listana pistelistoja
            X_test_matrix: testidata listana matriiseja
            n: testidatajoukon koko
            m: opetusdatajoukon koko
            layrs: laskennessa käytettävien kerrosten määrä
            sdm: "lähellä" olevien pisteiden neliölliset etäisyydet haetaan
                  valmiiksi lasketusta arrays.py tiedostosta funktio-kutsujen välttämiseksi
            point_list: pistelista, joka vastaan sdm-matriisen etäisyyksiä pienimmästä suurimpaan
            """

    def __init__(self, X_train_points, X_train_matrix, Y_train,
                 X_test_points, X_test_matrix, k=3, layers=4):
        """konstruktori
        Args:
            X_train_points: X train kuvat listana pistelistoja
            X_train_matrix: X train kuvat listana matriiseja
            Y_train: Y train ominaisuudet (0-9) listana
            X_test_points: X test kuvat listana pistelistoja
            X_test_matrix: X test kuvat listana matriiseja
            k: määrittää k-lähintä naapuria
            layers: laskennassa käytettävien kerrosten määrä"""
        self.k = k
        self.X_train_points = X_train_points
        self.X_train_matrix = X_train_matrix
        self.Y_train = Y_train
        self.X_test_points = X_test_points
        self.X_test_matrix = X_test_matrix
        self.n = len(self.X_test_points)
        self.m = len(self.X_train_points)
        self.layers = layers
        self.sdm = SDM[layers-1]
        self.point_list = PL[layers-1]

    def predict3(self):
        """KNN ennustamat ominaisuudet (numero 0-9)
            toteutus minimikekona
            hausdorffin etäisyyden laskenta sisäänrakennettu funktioon
            logiikkaa avattu lisää kommenteissa
        Returns:
            Y_pred: lista ennustettuja ominaisuuksia
        """
        Y_pred = []
        # käydään läpi jokainen kuva pistejoukossa
        for test_index in range(self.n):
            heap = []
            # kullekin kuvalle lasketaan etäisyys koko opetusjoukkoon
            for train_index in range(self.m):
                sum_AB = 0
                # ensimmäisen tarkastetaan onko opetuskuvassa
                # sama piste kuin tutkittava piste
                # jos on summa ei muutu -> siirrytään seuraavaan pisteeseen
                for a in self.X_test_points[test_index]:
                    not_found = True
                    if self.X_train_matrix[train_index][a[0]][a[1]]:
                        continue
                    # seuraavaksi haetaan lähellä olevista pisteistä
                    # jos löytyy, arvo valmiiksi lasketusta etäisyysmatriisista
                    # "layers" parametri määrittää kuin isosta joukosta haku tehdään
                    for close in self.point_list:
                        if (close[0] + a[0] < 0 or close[0] + a[0] > 27
                                or close[1] + a[1] < 0 or close[1]+a[1] > 27):
                            continue
                        if self.X_train_matrix[train_index][close[0]+a[0]][close[1]+a[1]]:
                            sum_AB += self.sdm[close[0] +
                                               self.layers][close[1]+self.layers]
                            not_found = False
                            break
                    # jos ei löytynyt, haetaan lähin piste käymällä läpi kaikki pisteet
                    # piste vs opetuskuva pistelistana ja heataan minimi
                    if not_found:
                        minimum = 1000000
                        # tämä minimin haku marginaalisesti parempi kuin muut vaihtoehdot
                        for b in self.X_train_points[train_index]:
                            minimum = min(minimum, (a[0]-b[0]) *
                                          (a[0]-b[0]) + (a[1]-b[1])*(a[1]-b[1]))
                        sum_AB += minimum

                # suunnattu etäisyys tarvitaan myös opetuskuvan jokaiselle pisteelle
                # vs testikuva
                # stepit ovat samat kuin yllä kuvatut
                sum_BA = 0
                for b in self.X_train_points[train_index]:
                    not_found = True
                    if self.X_test_matrix[test_index][b[0]][b[1]]:
                        continue
                    for close in self.point_list:
                        if (close[0] + b[0] < 0 or close[0] + b[0] > 27
                                or close[1] + b[1] < 0 or close[1]+b[1] > 27):
                            continue
                        if self.X_test_matrix[test_index][close[0]+b[0]][close[1]+b[1]]:
                            sum_BA += self.sdm[close[0] +
                                               self.layers][close[1]+self.layers]
                            not_found = False
                            break
                    if not_found:
                        minimum = 1000000
                        for a in self.X_test_points[test_index]:
                            minimum = min(minimum, (a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1]))
                        sum_BA += minimum
                # suuntaamattomana etäisyytenä käytetään tässä summaa d(A,B)+d(B,A)
                # muita Hausdorff etäisyyksiä hakiessä tämä pitää muuttaa
                # vaihtoehdot jätetty alle kommentoituina riveinä

                d = sum_AB + sum_BA
                #d = self.n*sum_AB + self.m*sum_BA #painotettu keskiarvo
                #d = min(sum_AB, sum_BA) #minimi
                #d = max(sum_AB, sum_BA) #maksimi

                # suuntaamaton etäisyys ja opetuskuvan indeksi kekoon
                heappush(heap, (d, train_index))
            neighbors = []
            # keosta haetaan k-lähintä etäisyyttä
            # ja näiden ominaisuudet lisätäään Y_pred listaan
            for _ in range(self.k):
                h = heappop(heap)
                neighbors.append(self.Y_train[h[1]])
            counter = Counter(neighbors).most_common(1)[0]
            Y_pred.append(counter[0])
        return Y_pred
