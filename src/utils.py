"""moduuli apufunktioita varten
apufunktioiden tarkoitus on nopeuttaa laskentaa:
näillä lasketaan valmiiksi matriisit sekä pistelistat,
jotta varsinainen laskenta ei tarvitse funktiokutsuja
"""
from math import sqrt
import numpy as np


def euclidean(a, b):
    """pisteiden a ja b [x,y] välinen
        normaali euklidinen etäisyys
    Args:
        a, b: pisteet (x,y) tupleina
    Returns:
        euklidinen etäisyys
    """
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)


def square_distance(a, b):
    """pisteiden a ja b [x,y] välinen
    neliöllinen etäisyys
    Args:
        a,b: pisteet (x,y) tupleina
    Returns:
        neliöllinen täisyys"""
    return (a[0]-b[0])**2+(a[1]-b[1])**2


def euclidean_dist_matrix(layers):
    """taulukkoon valmiiksi laskettuna keskipisteestä
        euklidiset etäisyydet layers kerrokselle
    Args:
        layers: kerrosten määrä
    Returns:
        dist_array: euklidiset etäisyydet np.arrayna"""
    center = (layers, layers)
    dist_array = np.empty([2*layers+1, 2*layers+1])
    for i in range(0, dist_array.shape[0]):
        for j in range(0, dist_array.shape[1]):
            dist_array[i][j] = euclidean(center, (i, j))
    return dist_array


def square_dist_matrix(layers):
    """taulukkoon valmiiksi laskettuna keskipisteestä
        neliölliset etäisyydet layers kerrokselle
    Args:
        layers: kerrosten määrä
    Returns:
        dist_array: neliölliset etäisyydet np.arrayna, kokonaislukuja"""
    center = (layers, layers)
    dist_array = np.empty([2*layers+1, 2*layers+1], dtype='int16')
    for i in range(0, dist_array.shape[0]):
        for j in range(0, dist_array.shape[1]):
            dist_array[i][j] = (square_distance(center, (i, j)))
    return dist_array


def list_of_indices(distance_array):
    """järjestetyn etäisyystaulukon indeksi (x,y) listana
    Args:
        etäisyysmatriisi: np.array
    Returns:
        lista tupleja (x,y) etäisyyksien mukaan järjestettynä
            indeksi 0, jätetään pois, koska pisteen etäisyys itseensä on aina
            nolla, eikä tätä tarvita
    """
    ind = np.unravel_index(np.argsort(
        distance_array, axis=None), distance_array.shape)
    center = distance_array.shape[0]//2
    no_of_points = ind[0].shape[0]
    ones = np.ones((no_of_points, ))
    ind = ind - center*ones

    ind = ind.astype('int16')
    lst = [tuple(x) for x in zip(ind[0], ind[1])]
    return lst[1:]
