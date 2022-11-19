"""moduli KNN luokkaa varten"""

from heapq import heappush, heappop
from collections import Counter
from utils import euclidean, euclidean_dist_matrix

class KNN:
    """"K:n lähimmän naapurin luokka sisältää myös funktion Hausdorffin etäisyyden laskemiseksi"""
    def __init__(self, X_train_points, X_train_matrix, Y_train, X_test_points, X_test_matrix, k=3):
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
        self.layers = 2 # ei voi jäädä näin, määriteltävä jossain järkevässä paikassa
        self.edm = euclidean_dist_matrix(layers=self.layers)

    def predict(self):
        """KNN ennustamat ominaisuudet (numero 0-9)
        toteutus listana"""
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
        toteutus minimikekona"""
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


    def hausdorff_distance(self, test_index, train_index):
        """Hausdorf etäisyys
            suunnattu funktio d6b (eli painottamaton summa)
            ja tässä vaiheessa suuntaamattoman etäisyyden funktio summana d(A,B)+d(B,A)
        """
        sum_AB=0

        Al=self.X_test_points[test_index]
        Am=self.X_test_matrix[test_index]
        Bl=self.X_train_points[train_index]
        Bm=self.X_train_matrix[train_index]

        for a in Al:
            #onko päällekkäinen piste?
            if Bm[a[0]][a[1]]: 
                break
            #etsitään ensin matriisista x kerrosta
            for i in range(max(a[0]-self.layers, 0), min(self.layers+a[0],27)): 
                for j in range(max(a[1]-self.layers, 0), min(self.layers+a[1], 27)):
                    if Bm[i][j]:
                        sum_AB += self.edm[i-a[0]][j-a[1]]
                        break
                    else:
                        continue
                    break
            #else: #jos ei löytynyt matriista, lasketaan etäisyydet pistelistoista
            sum_AB += self.dist_point_set_all(a, Bl)

        sum_BA=0
        for b in Bl: #sama kuin yllä suuntaan BA
            if Am[b[0]][b[1]]:
                break
            for i in range(max(b[0]-self.layers, 0), min(self.layers+b[0],27)):
                for j in range(max(b[1]-self.layers, 0), min(self.layers+b[1], 27)):
                    if Am[i][j]:
                        sum_BA += self.edm[i-b[0]][j-b[1]]
                        break
                    else:
                        continue
                    break
            #else:
            sum_BA += self.dist_point_set_all(b, Al)
        return sum_AB+sum_BA

    @staticmethod
    def dist_point_set_all(a,B):
        """pisteen ja pistejoukon minimietäisyyden laskenta toistaiseksi omana funktionaan"""
        return min([euclidean(a,b) for b in B])
