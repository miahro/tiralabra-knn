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
    Attributes:
        X_test: opetusdata listana matriiseja
        X_test_point_list: opetusdata listana pistelistoja
        X_train: testidata listana matriiseja
        X_X_train_point_list: testidata listana pistelistoja
        Y_test: testidatan ominaisuudet listana
        Y_train: opetusdatan ominaisuudet listana

    """

    def __init__(self, filter_value):
        """alustaa Mnist -olion
        Args:
            filter_value: harmaasuodattimen arvo, tätä pienemmät nollataan
                    suurempien tai yhtäsuurten arvo 1

        datan lukuvaiheessa käytetään np.arrayta, mutta
        lopussa np.array:t konvertoidaan normaaleiksi listoiksi,
        koska näiden käsittely laskennassa on nopeampaa
                    """
        X_train_temp = self.download(TRAIN_X_URL)[0x10:].reshape((-1, 28, 28))
        self.Y_train = self.download(TRAIN_Y_URL)[8:].tolist()
        X_test_temp = self.download(TEST_X_URL)[0x10:].reshape((-1, 28, 28))
        self.Y_test = self.download(TEST_Y_URL)[8:].tolist()
        X_train_filt_temp = X_train_temp >= filter_value
        self.X_train = X_train_filt_temp.tolist()
        self.X_train_point_list = [np.transpose(
            np.nonzero(x)).tolist() for x in self.X_train]
        X_test_filt_temp = X_test_temp >= filter_value
        self.X_test = X_test_filt_temp.tolist()
        self.X_test_point_list = [np.transpose(
            np.nonzero(x)).tolist() for x in self.X_test]

    @staticmethod
    def download(url):
        """lataa MNIST datan datatiedostoon, jos ei jo ladattu
        jos ladattu lukee paikallisesta datatiedostosta
        Args:
            url: MNIST datan www-osoite
        Returns:
            palauttaa kuvat numpy arrayna
        """
        if not os.path.exists(DATAFILEPATH):
            os.makedirs(DATAFILEPATH)
        fp = os.path.join(DATAFILEPATH, hashlib.md5(
            url.encode('utf-8')).hexdigest())
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
            Args:
                start, stop: osajoukon alku- ja loppuindekset
            Returns:
                osajoukko opetusdatasta, lista matriiseja'''
        return self.X_train[start:end]

    def X_train_list(self, start=0, end=60000):
        '''palauttaa X_train kuvat pistelistana
            Args:
                start, stop: osajoukon alku- ja loppuindeksit
            Returns:
                osajoukko opetusdatasta, lista pisteitä'''
        return self.X_train_point_list[start:end]

    def X_test_matrix(self, start=0, end=10000):
        '''palauttaa X_test kuvat matriisina
            Args:
                start, stop: osajoukon alku- ja loppuindekset
            Returns:
                osajoukko testidatasta, lista matriiseja'''
        return self.X_test[start:end]

    def X_test_list(self, start=0, end=10000):
        '''palauttaa X_test kuvat pistelistana
            Args:
                start, stop: osajoukon alku- ja loppuindeksit
            Returns:
                osajoukko testidatasta, lista pisteitä'''
        return self.X_test_point_list[start:end]

    def Y_train_labels(self, start=0, end=60000):
        '''palauttaa  Y_train ominaisuudet
            Args:
                start, stop: osajoukon alku- ja loppuindeksit
            Returns:
                opetusdatan ominaisuudet, listana'''

        return self.Y_train[start:end]

    def Y_test_labels(self, start=0, end=10000):
        '''palauttaa  Y_test ominaisuudet
            Args:
                start, stop: osajoukon alku- ja loppuindeksit
            Returns:
                testidatan ominaisuudet, listana'''
        return self.Y_test[start:end]
