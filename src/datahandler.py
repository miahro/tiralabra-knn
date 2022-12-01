"""sisältää DataHandler luokan"""
import csv
import os
from mnistdata import Mnistdata
from KNN import KNN
#from utils import square_dist_matrix, list_of_indices
from timer import Timer
from config import OUTPUTFILEPATH


class DataHandler:
    """ylätason luokka joka kutsuu Mnistdata luokan oliolta
    MNIST tietokantadatan formatuituna käyttökelpoiseen muotoon
    toimittaa valitun osan siitä KNN oliolle laskentaa varten
    ja käsittelee KNN olion predict -funktion toimittamat tulokset
    DataHandler ei siis suorita varsinaista lastentaa
    """

    def __init__(self):
        """konstruktori alustaa luokan muuttujat tyhjiksi"""
        self.X_train_point_list = None
        self.X_train_matrix = None
        self.X_test_point_list = None
        self.X_test_matrix = None
        self.Y_train = None
        self.Y_test = None
        self.Y_predicted = None
        self.knn = None
        self.filter_value = 128  # oletusarvo
        self.timer = Timer()
        self.initialized = False
        self.test_index_start = None
        self.test_index_end = None
        self.train_index_start = None
        self.train_index_end = None
        self.k = None
        self.layers = None
        self.mnist = None

    def read_mnist(self):
        """lukee Mnist tietokannan"""
        self.mnist = Mnistdata(filter_value=self.filter_value)

    def set_filter(self, filter_value):
        """harmaasuodattimen arvo voidaan asettaa tästä, ennen MNIST datan lukemista"""
        self.filter_value = filter_value

    def set_parameters(self, test_index_start, test_index_end,
                       train_index_start, train_index_end, k=3, layers=4):
        """asetetaan parametrit, joiden perusteella KNN olio luodaan"""
        self.test_index_start = test_index_start
        self.test_index_end = test_index_end
        self.train_index_start = train_index_start
        self.train_index_end = train_index_end
        self.k = k
        self.layers = layers

    def init_knn(self):
        """hakee MNIST datasta määritellyt joukot testi ja opetusdataa
        alustaa KNN-olion näiden joukkojen perusteella"""
        self.X_train_point_list = self.mnist.X_train_list(
            start=self.train_index_start, end=self.train_index_end)
        self.X_train_matrix = self.mnist.X_train_matrix(
            start=self.train_index_start, end=self.train_index_end)
        self.X_test_point_list = self.mnist.X_test_list(
            start=self.test_index_start, end=self.test_index_end)
        self.X_test_matrix = self.mnist.X_test_matrix(
            start=self.test_index_start, end=self.test_index_end)
        self.Y_train = self.mnist.Y_train_labels(
            start=self.train_index_start, end=self.train_index_end)
        self.Y_test = self.mnist.Y_test_labels(
            start=self.test_index_start, end=self.test_index_end)
        self.knn = KNN(self.X_train_point_list, self.X_train_matrix, self.Y_train,
                       self.X_test_point_list, self.X_test_matrix, self.k, self.layers)
        self.initialized = True

    def predict(self):
        """kutsuu KNN:n predict3 funktiota
        tämä suorittaa kaiken varsinaisen laskennan"""
        self.timer.start()
        self.Y_predicted = self.knn.predict3()
        self.timer.stop()

    def evaluate(self):
        """palauttaa KNN:n tulokset sanakirjana"""
        if self.Y_predicted is None:
            return {}
        wrong_ind = []
        for i in range(len(self.Y_test)):
            if self.Y_test[i] != self.Y_predicted[i]:
                wrong_ind.append(i)
        wrong_ind_orig_mnist = []
        for i in range(len(wrong_ind)):
            wrong_ind_orig_mnist.append(wrong_ind[i]+self.test_index_start)
        wrong_nos = []
        for i in range(len(wrong_ind)):
            wrong_nos.append(self.Y_test[wrong_ind[i]])
        return {"test_index_start": self.test_index_start, "test_index_end": self.test_index_end,
                "train_index_start": self.train_index_start,
                "train_index_end": self.train_index_end,
                "Y_test": self.Y_test, "Y_predicted": self.Y_predicted,
                "correct": len(self.Y_test)-len(wrong_ind),
                "wrong": len(wrong_ind), "wrong_ind": wrong_ind, "wrong_nos": wrong_nos,
                "wrong_orig_mnist": wrong_ind_orig_mnist, "runtime": self.timer.result(),
                "k-value": self.k, "filter": self.filter_value, "layers": self.layers}

    def write_results_to_file(self):
        """tallentaa KNN:n tulokset .csv tiedostoon"""
        # print(OUTPUTFILEPATH)
        result = self.evaluate()
        keys = result.keys()
        if not os.path.isfile(OUTPUTFILEPATH):
            with open(OUTPUTFILEPATH, 'w', encoding='utf-8') as csvfile:
                csvwriter = csv.DictWriter(
                    csvfile, fieldnames=keys, delimiter=';')
                csvwriter.writeheader()

        with open(OUTPUTFILEPATH, 'a', encoding='utf-8') as csvfile:
            csvwriter = csv.DictWriter(csvfile, fieldnames=keys, delimiter=';')
            csvwriter.writerow(result)


datahandler = DataHandler()
