"""moduli KNN luokkaa varten"""

from heapq import heappush, heappop
from collections import Counter
from utils import euclidean, euclidean_dist_matrix, euclidean_4D

point_list = [(-1, 0), (1,0), (0,-1), (0,1), (-1,-1), (1,1), (-1,1), (1,-1),
                        (2,0), (-2,0), (0,-2), (0,2), (-1, -2), (-1, 2), (1,-2), (1,2),
                        (-2, -1), (-2,1), (2,-1), (2,1), (-2,-2), (-2,2), (2,-2), (2,2),
                        ]


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
        self.e4d = euclidean_4D(28)
        self.counter0=0
        self.counter1=0
        self.counter2=0
        self.counter3=0
        self.counter4=0
        self.counter5=0


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

    def predict3(self):
        """KNN ennustamat ominaisuudet (numero 0-9)
        toteutus minimikekona"""
        Y_pred = []
        for test_index in range(self.n):
            heap=[]
            for train_index in range(self.m):
                self.counter0 += 1
                sum_AB=0
                for a in self.X_test_points[test_index]:
                    not_found = True
                    self.counter1 += 1
                    #onko päällekkäinen piste?
                    if self.X_train_matrix[train_index][a[0]][a[1]]: 
                        self.counter2 += 1
                        not_found = False
                        continue
                    self.counter3+=1
                    for close in point_list:
                        if close[0] + a[0 ]<0 or close[0]+ a[0]>27 or close[1] + a[1]<0 or close[1]+a[1]>27:
                            continue
                        if self.X_train_matrix[train_index][close[0]+a[0]][close[1]+a[1]]:
                                self.counter4 +=1 
                                sum_AB += self.edm[close[0]+2][close[1]+2]
                                not_found = False
                                break
                    if not_found:
                        self.counter5 += 1       
                        sum_AB += min([euclidean(a,b) for b in self.X_train_points[train_index]])                

                sum_BA=0
                for b in self.X_train_points[train_index]:
                    not_found = True
                    self.counter1 += 1
                    if self.X_test_matrix[test_index][b[0]][b[1]]: 
                        self.counter2 += 1
                        continue
                    self.counter3+=1
                    for close in point_list:
                        if close[0] + b[0 ]<0 or close[0]+ b[0]>27 or close[1] + b[1]<0 or close[1]+b[1]>27:
                            continue
                        if self.X_test_matrix[test_index][close[0]+b[0]][close[1]+b[1]]:
                                self.counter4 +=1 
                                sum_BA += self.edm[close[0]+2][close[1]+2]
                                not_found = False
                                break
                    if not_found:
                        self.counter5 += 1                        
                        sum_BA += min([euclidean(b,a) for a in self.X_test_points[test_index]])




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

#        Al=self.X_test_points[test_index]
#        Am=self.X_test_matrix[test_index]
#        Bl=self.X_train_points[train_index]
#        Bm=self.X_train_matrix[train_index]
        self.counter0 +=1
#        print(len(Al))
#        for a in Al:
        for a in self.X_test_points[test_index]:
            not_found = True
            self.counter1 += 1
            #onko päällekkäinen piste?
            if self.X_train_matrix[train_index][a[0]][a[1]]: 
                self.counter2 += 1
                not_found = False
                continue
#            etsitään ensin matriisista x kerrosta
            self.counter3+=1
            for close in point_list:
                if close[0] + a[0 ]<0 or close[0]+ a[0]>27 or close[1] + a[1]<0 or close[1]+a[1]>27:
                    continue
                if self.X_train_matrix[train_index][close[0]+a[0]][close[1]+a[1]]:
                        self.counter4 +=1 
                        sum_AB += self.edm[close[0]+2][close[1]+2]
                        not_found = False
                        break

            if not_found:
                self.counter5 += 1
#               sum_AB=0
                sum_AB += min([euclidean(a,b) for b in self.X_train_points[train_index]])
         


        sum_BA=0
        for b in self.X_train_points[train_index]:
            not_found = True
            self.counter1 += 1
            #onko päällekkäinen piste?
            if self.X_test_matrix[test_index][b[0]][b[1]]: 
                self.counter2 += 1
                continue
            # #etsitään ensin matriisista x kerrosta
            self.counter3+=1
            for close in point_list:
                if close[0] + b[0 ]<0 or close[0]+ b[0]>27 or close[1] + b[1]<0 or close[1]+b[1]>27:
                    continue
                if self.X_test_matrix[test_index][close[0]+b[0]][close[1]+b[1]]:
                        self.counter4 +=1 
                        sum_BA += self.edm[close[0]+2][close[1]+2]
                        not_found = False
                        break
                # else:
                #     continue
                # break
            if not_found:
                self.counter5 += 1
                sum_BA += min([euclidean(b,a) for a in self.X_test_points[test_index]])

#                sum_AB += self.dist_point_set_all(b, self.X_test_points[test_index])



        return sum_AB+sum_BA

    #@staticmethod
    def dist_point_set_all(self,a,B):
        """pisteen ja pistejoukon minimietäisyyden laskenta toistaiseksi omana funktionaan"""
#        return min([euclidean(a,b) for b in B])
        minimum = 1000000
        self.counter5 += 1
        for b in B:
            dist = euclidean(a,b)
            if minimum > dist:
                minimum = dist
        return minimum

