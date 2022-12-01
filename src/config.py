"""moduli sisältää vakioarvoja kuten
datan www-osoitteet, data ja tulostiedoston polut
sekä oletusparametrit käyttöliittymän parametrinäkymää varten"""
import os

directory = os.path.dirname(__file__)

"""konfigurointitiedot, vakioita"""

TRAIN_X_URL = "http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz"
TRAIN_Y_URL = "http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz"
TEST_X_URL = "http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz"
TEST_Y_URL = "http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz"

DATAFILEPATH = os.path.join(directory, '..', 'data')

OUTPUTFILEPATH = os.path.join(directory, '..', "data/knn_results.csv")


# oletusparametrit käyttöliittymää varten
parameters = {
    "test_index_start": 0,
    "test_index_end": 1,
    "train_index_start": 0,
    "train_index_end":  100,
    "k_value": 3,
    "layers": 4
}
