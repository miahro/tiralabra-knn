"""moduuli MNIST datan lukemista varten
käyttää valmista python-mnist pakettia raakadan lukemiseen
"""

from pathlib import Path
from mnist import MNIST
import numpy as np



class Mnistrawdata:
    """luokka MNIST raakadatan lukemista varten
    lukee MNIST tiedostot data_folder hakemistosta (tiedon kopiointia varten .sh sripti)
    muuttaa kuvadatan np.arrayksi
    muuntaa harmaasävyn mustavalkoiseksi konstruktorille annetun filter_valuen perusteella
    muuntaa kuvadatan pistejouksi (ts mustat pisteet (x,y)).
    samat toimet X_train ja X_test. Y_train ja Y_test vain luetaan ja muunnetaan np.arrayksi.
    """

    def __init__(self, filter_value):
        data_folder = Path("data/") #ei hyvä tapa, ok toistaiseksi, korjataan myöhemmin
        m = MNIST(path=data_folder)
        training = m.load_training()

        training_x =  [np.asarray(X).reshape(28,28) for X in training[0]]
        training_x_filtered = [np.nonzero(x >= filter_value) for x in training_x]
        self.X_train = [np.array(list(zip(X[0], X[1]))) for X in training_x_filtered]
        self.Y_train = training[1]

        testing = m.load_testing()
        testing_x =  [np.asarray(X).reshape(28,28) for X in testing[0]]
        testing_x_filtered = [np.nonzero(x >= filter_value) for x in testing_x]
        self.X_test = [np.array(list(zip(X[0], X[1]))) for X in testing_x_filtered]
        self.Y_test = testing[1]

    def read_training_x(self, start=0, end=60000):
        "palauttaa välin start-end X_train pisteistä"
        return self.X_train[start:end]

    def read_training_y(self, start=0, end=60000):
        "palauttaa välin start-end Y_train arvoista (ominaisuuksista)"
        return self.Y_train[start:end]

    def read_testing_x(self, start=0, end=10000):
        "palauttaa välin start-end X_test pisteistä"
        return self.X_test[start:end]

    def read_testing_y(self, start=0, end=10000):
        "palauttaa välin start-end Y_test arvoista (ominaisuuksista)"
        return self.Y_test[start:end]
