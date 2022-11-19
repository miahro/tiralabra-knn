"""moduuli apufunktioita varten"""
from math import sqrt
import numpy as np

def euclidean(a, b):
    """pisteiden a ja b [x,y] välinen
        normaali euklidinen etäisyys
    """
    #return ((a[0]-b[0])**2+(a[1]-b[1])**2)
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)


def euclidean_dist_matrix(layers):
    """taulukkoon valmiiksi laskettuna keskipisteestä
        euklidiset etäisyydet layers kerrokselle"""
    center = (layers, layers)
    dist_array = np.empty([2*layers+1, 2*layers+1])
    for i in range(0, dist_array.shape[0]):
        for j in range(0, dist_array.shape[1]):
            dist_array[i][j] = euclidean(center, (i,j))
    return dist_array
        