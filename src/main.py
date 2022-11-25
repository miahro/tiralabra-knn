
import sys
sys.path.append(".")

from read_mnist import Mnistrawdata
from timer import Timer
from directedhausdorff import DirectedHausdorff
from undirectedhausdorff import UndirectedHausdorff
from math import sqrt
import numpy as np
from testcases import A, B, C, A2, C2, Am, Bm, A2m, Cm, C2m
import mnistdata
from mnistdata import Mnistdata
from utils import euclidean_dist_matrix, euclidean,  list_of_indices, square_dist_matrix
import requests, gzip, os, hashlib
import hausdorff
from hausdorff import Hausdorff
from datahandler import DataHandler

from KNN import KNN

"""Main program for early development phase
    to be replaced with proper UI later
"""


def main():
  
    """development phase function calls here
        to be replaced with ui
    """
    n_start=190
    n=10
    m=400


    mnt=Mnistdata(filter_value=128)
    X_train_matrix = mnt.X_train_matrix(start=0, end=m)
    X_train_list = mnt.X_train_list(start=0, end=m)
    Y_train = mnt.Y_train_labels(start=0, end=m)
    X_test_matrix = mnt.X_test_matrix(start=n_start, end=n_start+n)
    X_test_list = mnt.X_test_list(start=n_start, end=n_start+n)
    Y_test = mnt.Y_test_labels(start=n_start, end=n_start+n)
    k = 3

    pl = [(1, 0), (0, 1), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1), (2, 0), (0, 2), (-2, 0), (0, -2), (-1, -2), (1, -2), (1, 2), (2, -1), (-2, -1), (-1, 2), (-2, 1), (2, 1), (2, -2), (-2, -2), (-2, 2), (2, 2), (0, 3), (0, -3), (-3, 0), (3, 0), (-3, 1), (1, 3), (3, 1), (-1, 3), (-1, -3), (3, -1), (-3, -1), (1, -3), (-2, 3), (-2, -3), (3, -2), (2, -3), (2, 3), (3, 2), (-3, 2), (-3, -2), (-4, 0), (0, 4), (4, 0), (0, -4), (4, 1), (-1, -4), (1, -4), (-1, 4), (4, -1), (-4, 1), (1, 4), (-4, -1), (-3, -3), (3, 3), (-3, 3), (3, -3), (4, -2), (-4, 2), (-2, -4), (2, -4), (-2, 4), (2, 4), (-4, -2), (4, 2), (-4, 3), (-3, 4), (-3, -4), (3, 4), (4, -3), (-4, -3), (3, -4), (4, 3), (-4, -4), (-4, 4), (4, -4), (4, 4)]

    knn3 = KNN(X_train_points=X_train_list, X_train_matrix=X_train_matrix, Y_train=Y_train, X_test_points=X_test_list, X_test_matrix=X_test_matrix, point_list=pl)

    t = Timer(cputime=True)


    t.start()
    result_Y3 =knn3.predict3()
    t.stop()
    print("runtime with predict3")
    t.result()

    print(f"correct {Y_test}")
    print(f"predict3 {result_Y3}")


    wrong=0
    for i in range(len(result_Y3)):
        if result_Y3[i] != Y_test[i]:
            wrong +=1
    print(f"väärin tunnistettuja {wrong}")

    dh=DataHandler()
    dh.set_parameters(190, 210, 0, 200, k=3, layers=4)
    dh.read_mnist()
    dh.init_knn()
    print("knn initiliasoitu laskenta alkaa")
    t.start()
    Yp=dh.predict()
    t.stop()
    t.result()
    print(dh.evaluate())

def test():
    a = 1
    da = square_dist_matrix(layers=4)
    print(type(da))
    print(da)
    print(list_of_indices(da))

#test()
main()

