
import sys
sys.path.append(".")

from read_mnist import Mnistrawdata
from timer import Timer
from directedhausdorff import DirectedHausdorff
from undirectedhausdorff import UndirectedHausdorff
from math import sqrt
import numpy as np
from testcases import A, B, Am, Bm
import mnistdata
from mnistdata import Mnistdata
from utils import euclidean_dist_matrix, euclidean
import requests, gzip, os, hashlib
import hausdorff
from hausdorff import Hausdorff

from KNN import KNN

"""Main program for early development phase
    to be replaced with proper UI later
"""

# edm =euclidean_dist_matrix(3)
# print(edm)

def dist_from_matrix(xy, B):
    if not B[xy[0]][xy[1]]:
        return 0
    else:
        for i in range(0, edm.shape[0]//2):
            for j in range(0, edm.shape[1]//2):
                if B[i][j]:
                    return edm[i][j]
                elif B[-i][j]:
                    return edm[-i][j]
                elif B[-i][-j]:
                    return edm[-i][-j]
                elif B[i][-j]:
                    return edm[i][-j]



def main():
  
    """development phase function calls here
        to be replaced with ui
    """


 
    n=30
    m=1000


    mnt=Mnistdata(filter_value=128)
    X_train_matrix = mnt.X_train_matrix(start=0, end=m)
    X_train_list = mnt.X_train_list(start=0, end=m)
    Y_train = mnt.Y_train_labels(start=0, end=m)

    X_test_matrix = mnt.X_test_matrix(start=0, end=n)
    X_test_list = mnt.X_test_list(start=0, end=n)

    knn = KNN(X_train_points=X_train_list, X_train_matrix=X_train_matrix, Y_train=Y_train, X_test_points=X_test_list, X_test_matrix=X_test_matrix, k=4)

    t=Timer(cputime=True)
    t.start()
    prd = knn.predict()
    t.stop()

    Y_test = mnt.Y_test_labels(start=0, end=n)
    print(prd)
    print(list(Y_test))

    t2=Timer(cputime=True)
    t2.start()
    prd2=knn.predict2()
    t2.stop()
    print(prd2)

    wrong_cnt=0
    for i in range(n):
        if int(prd[i])-int(list(Y_test)[i]) != 0:
            wrong_cnt += 1
    print(f"wrong: {wrong_cnt}")

    wrong_cnt=0
    for i in range(n):
        if int(prd2[i])-int(list(Y_test)[i]) != 0:
            wrong_cnt += 1
    print(f"wrong prd2: {wrong_cnt}")


    t.result()
    t2.result()



main()

