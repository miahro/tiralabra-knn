"""moduli KNN luokkaa varten"""

from heapq import heappush, heappop
from collections import Counter
from utils import  square_distance, square_dist_matrix
from arrays import SDM, PL

class KNN:
    """"K:n lähimmän naapurin luokka sisältää myös funktion Hausdorffin etäisyyden laskemiseksi"""
    def __init__(self, X_train_points, X_train_matrix, Y_train, X_test_points, X_test_matrix, k=3, layers=4):
        """konstruktori
        Args:   X_train_points: X train kuvat pistelistamuodossa
                X_train_matrix: X train kuvat matriisina
                Y_train: Y train ominaisuudet (0-9) listana
                X_test_points: X test kuvat pistelistamuodossa
                X_test_matrix: X test kuvat matriisina
                k: määrittää k-lähintä naapuria"""
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
#        self.sdm = square_dist_matrix(layers)

    def predict(self):
        """KNN ennustamat ominaisuudet (numero 0-9)
        toteutus listana
        kutsuu hausdorffin etäisyyttä funktiona
        kehitysvaiheeheen funktio tulosten oikeellisuuden tarkastamiseksi
        """
        Y_pred = []
        for i in range(self.n):
            distance=[]
            for j in range(self.m):
                d = self.hausdorff_distance(i, j)
                distance.append((d, self.Y_train[j]))
            distance=sorted(distance)
            neightbors = []
            for item in range(self.k):
                neightbors.append(distance[item][1])
            counter = Counter(neightbors).most_common(1)[0]
            Y_pred.append(counter[0])
        return Y_pred

    def predict2(self):
        """KNN ennustamat ominaisuudet (numero 0-9)
        toteutus minimikekona
        kutsuu hausdorffin etäisyyttä funktiona
        kehitysvaiheeheen funktio tulosten oikeellisuuden tarkastamiseksi
        """
        Y_pred = []
        for i in range(self.n):
            heap=[]
            for j in range(self.m):
                d = self.hausdorff_distance(i, j)
                heappush(heap, (d,j))
            neighbors = []
            for _ in range(self.k):
                h = heappop(heap)
                neighbors.append(self.Y_train[h[1]])
            counter = Counter(neighbors).most_common(1)[0]
            Y_pred.append(counter[0])
        return Y_pred

    def predict3(self):
        """KNN ennustamat ominaisuudet (numero 0-9)
        toteutus minimikekona
        hausdorffin etäisyyden laskenta sisäänrakennettu funktioon
        """
        Y_pred = []
        for test_index in range(self.n):
            heap=[]
            for train_index in range(self.m):
                sum_AB=0
                for a in self.X_test_points[test_index]:
                    not_found = True
                    if self.X_train_matrix[train_index][a[0]][a[1]]:
                        continue
                    for close in self.point_list:
                        if close[0] + a[0 ]<0 or close[0]+ a[0]>27 or close[1] + a[1]<0 or close[1]+a[1]>27:
                            continue
                        if self.X_train_matrix[train_index][close[0]+a[0]][close[1]+a[1]]:
                            sum_AB += self.sdm[close[0]+self.layers][close[1]+self.layers]
                            not_found = False
                            break
                    if not_found:
                        minimum = 1000000
                        for b in self.X_train_points[train_index]:
                            temp = (a[0]-b[0])**2+(a[1]-b[1])**2
                            if temp < minimum:
                                minimum = temp
                        sum_AB += minimum

                sum_BA=0
                for b in self.X_train_points[train_index]:
                    not_found = True
                    if self.X_test_matrix[test_index][b[0]][b[1]]:
                        continue
                    for close in self.point_list:
                        if close[0] + b[0 ]<0 or close[0]+ b[0]>27 or close[1] + b[1]<0 or close[1]+b[1]>27:
                            continue
                        if self.X_test_matrix[test_index][close[0]+b[0]][close[1]+b[1]]:
                            sum_BA += self.sdm[close[0]+self.layers][close[1]+self.layers]
                            not_found = False
                            break
                    if not_found:
                        minimum = 1000000
                        for a in self.X_test_points[test_index]:
                            temp = (a[0]-b[0])**2+(a[1]-b[1])**2
                            if temp < minimum:
                                minimum = temp
                        sum_BA += minimum

                d = sum_AB + sum_BA
                heappush(heap, (d,train_index))
            neighbors = []
            for _ in range(self.k):
                h = heappop(heap)
                neighbors.append(self.Y_train[h[1]])
            counter = Counter(neighbors).most_common(1)[0]
            Y_pred.append(counter[0])
        return Y_pred



    def hausdorff_distance(self, test_index, train_index):
        """Hausdorf etäisyys
            suunnattu funktio d6b (eli painottamaton summa)
            ja tässä vaiheessa suuntaamattoman etäisyyden funktio summana d(A,B)+d(B,A)
        """
        sum_AB=0

        for a in self.X_test_points[test_index]:
            not_found = True
            if self.X_train_matrix[train_index][a[0]][a[1]]:
                continue
            for close in self.point_list:
                if close[0] + a[0 ]<0 or close[0]+ a[0]>27 or close[1] + a[1]<0 or close[1]+a[1]>27:
                    continue
                if self.X_train_matrix[train_index][close[0]+a[0]][close[1]+a[1]]:
                    sum_AB += self.sdm[close[0]+self.layers][close[1]+self.layers]
                    not_found = False
                    break

            if not_found:
                sum_AB += min([square_distance(a,b) for b in self.X_train_points[train_index]])

        sum_BA=0
        for b in self.X_train_points[train_index]:
            not_found = True
            if self.X_test_matrix[test_index][b[0]][b[1]]:
                continue
            for close in self.point_list:
                if close[0] + b[0 ]<0 or close[0]+ b[0]>27 or close[1] + b[1]<0 or close[1]+b[1]>27:
                    continue
                if self.X_test_matrix[test_index][close[0]+b[0]][close[1]+b[1]]:
                    sum_BA += self.sdm[close[0]+self.layers][close[1]+self.layers]
                    not_found = False
                    break
            if not_found:
                sum_BA += min([square_distance(b,a) for a in self.X_test_points[test_index]])

        return sum_AB+sum_BA
