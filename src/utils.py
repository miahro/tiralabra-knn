"""moduuli apufunktioita varten"""
from math import sqrt
import numpy as np


def euclidean(a, b):
    """pisteiden a ja b [x,y] välinen
        normaali euklidinen etäisyys
    """
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)


def square_distance(a, b):
    """pisteiden a ja b [x,y] välinen
    neliöllinen etäisyys"""
    return (a[0]-b[0])**2+(a[1]-b[1])**2


def euclidean_dist_matrix(layers):
    """taulukkoon valmiiksi laskettuna keskipisteestä
        euklidiset etäisyydet layers kerrokselle"""
    center = (layers, layers)
    dist_array = np.empty([2*layers+1, 2*layers+1], dtype='int16')
    for i in range(0, dist_array.shape[0]):
        for j in range(0, dist_array.shape[1]):
            dist_array[i][j] = int(euclidean(center, (i, j)))
    return dist_array


def square_dist_matrix(layers):
    """taulukkoon valmiiksi laskettuna keskipisteestä
        neliölliset etäisyydet layers kerrokselle"""
    center = (layers, layers)
    dist_array = np.empty([2*layers+1, 2*layers+1], dtype='int16')
    for i in range(0, dist_array.shape[0]):
        for j in range(0, dist_array.shape[1]):
            dist_array[i][j] = (square_distance(center, (i, j)))
    return dist_array


def list_of_indices(distance_array):
    """järjestetyn etäisyystaulukon indeksi (x,y) listana"""
    ind = np.unravel_index(np.argsort(
        distance_array, axis=None), distance_array.shape)
    center = distance_array.shape[0]//2
    no_of_points = ind[0].shape[0]
    ones = np.ones((no_of_points, ))
    ind = ind - center*ones

    ind = ind.astype('int16')
    lst = [tuple(x) for x in zip(ind[0], ind[1])]
    return lst[1:]
