import unittest
from utils import euclidean, euclidean_dist_matrix, square_distance, square_dist_matrix, list_of_indices
from math import sqrt 

def test_euclidean():
    assert euclidean((0,0), (1,1)) - sqrt(2) <1e-10
    assert euclidean((0,0), (1,0)) - 1 <1e-10
    assert euclidean((1,1), (-1, -1)) -sqrt(8) < 1e-10

def test_euclidean_dist_matrix():
    test_matrix = euclidean_dist_matrix(3)
    assert test_matrix[3][3] - 0 < 1e-10
    assert test_matrix[0][0] - sqrt(18) < 1e-10
    assert test_matrix[1][5] - sqrt(8) < 1e-10
    assert test_matrix[5][6] - sqrt(13) < 1e-10
    assert test_matrix[1][6] - sqrt(13) < 1e-10
    assert test_matrix[6][2] - sqrt(10) < 1e-10


def test_square_dist():
    assert square_distance((0,0), (1,1)) == 2 
    assert square_distance((0,0), (1,0)) == 1 
    assert square_distance((1,1), (-1, -1)) == 8

def test_square_dist_matrix():
    test_matrix = square_dist_matrix(3)
    assert test_matrix[3][3] == 0  
    assert test_matrix[0][0] == 18 
    assert test_matrix[1][5] == 8 
    assert test_matrix[5][6] == 13 
    assert test_matrix[1][6] == 13 
    assert test_matrix[6][2] == 10 

def test_list_of_indices():
    test_matrix = square_dist_matrix(3)
    lst = list_of_indices(test_matrix)
    assert lst[0] in [(1,0), (0,1), (-1,0), (0,-1)]