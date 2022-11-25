"""moduuli MNIST tietokannan lukua varten"""
import gzip
import os
import hashlib
import requests
import numpy as np
from config import TRAIN_X_URL, TRAIN_Y_URL, TEST_X_URL, TEST_Y_URL, DATAFILEPATH



class Mnistdata:
    """Luokka MNIST datan lukemista varten
    lataa ja lukee MNIST datan
    suodattaa harmaasävykuvat mustavalkoisiksi
    annetulla filtterin arvolla (1-255)
    tallettaa datan kahteen tietorakenteeseen:
    1) numpu arrayksi (60k/10k kuvaa, x, y) xy = 28*28
    2) pistelistaksi
    sekä Y labelit 60k/10k numpy arrayna
    """

    def __init__(self, filter_value):
        X_train_temp = self.download(TRAIN_X_URL)[0x10:].reshape((-1, 28, 28))
        self.Y_train = self.download(TRAIN_Y_URL)[8:].tolist()
        X_test_temp = self.download(TEST_X_URL)[0x10:].reshape((-1, 28, 28))
        self.Y_test = self.download(TEST_Y_URL)[8:].tolist()
        X_train_filt_temp = X_train_temp >= filter_value
        self.X_train = X_train_filt_temp.tolist()

#        self.X_train = list(X_train_filt_temp)
        self.X_train_point_list = [np.transpose(np.nonzero(x)).tolist() for x in self.X_train]
        X_test_filt_temp = X_test_temp >= filter_value
#        self.X_test = list(X_test_filt_temp)
        self.X_test = X_test_filt_temp.tolist()
        self.X_test_point_list = [np.transpose(np.nonzero(x)).tolist() for x in self.X_test]

    @staticmethod
    def download(url):
        """lataa MNIST datan datatiedostoon, jos ei jo ladattu
        jos ladattu lukee paikallisesta datatiedostosta
        palauttaa kuvat numpy arrayna
        """
        fp = os.path.join(DATAFILEPATH, hashlib.md5(url.encode('utf-8')).hexdigest())
        if os.path.isfile(fp):
            with open(fp, "rb") as f:
                data = f.read()
        else:
            with open(fp, "wb") as f:
                data = requests.get(url).content
                f.write(data)
        return np.frombuffer(gzip.decompress(data), dtype=np.uint8).copy()

    def X_train_matrix(self, start=0, end=60000):
        '''palauttaa X_train kuvat matriirimuodossa
            Args: start, stop: voidaan määritellä palautettava osajoukko'''
        return self.X_train[start:end]

    def X_train_list(self, start=0, end=60000):
        '''palauttaa X_train kuvat pistelistana
            Args: start, stop: voidaan määritellä palautettava osajoukko'''
        return self.X_train_point_list[start:end]

    def X_test_matrix(self, start=0, end=10000):
        '''palauttaa X_test kuvat matriisina
            Args: start, stop: voidaan määritellä palautettava osajoukko'''
        return self.X_test[start:end]

    def X_test_list(self, start=0, end=10000):
        '''palauttaa X_test kuvat pistelistana
            Args: start, stop: voidaan määritellä palautettava osajoukko'''
        return self.X_test_point_list[start:end]

    def Y_train_labels(self, start=0, end=60000):
        '''palauttaa  Y_train ominaisuudet
            Args: start, stop: voidaan määritellä palautettava osajoukko'''
        return self.Y_train[start:end]

    def Y_test_labels(self, start=0, end=10000):
        '''palauttaa  Y_test ominaisuudet
            Args: start, stop: voidaan määritellä palautettava osajoukko'''
        return self.Y_test[start:end]
