import os
from dotenv import load_dotenv

directory = os.path.dirname(__file__)

"""konfigurointitiedot, vakioita"""

TRAIN_X_URL = "http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz"
TRAIN_Y_URL = "http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz"
TEST_X_URL = "http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz"
TEST_Y_URL = "http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz"
DATAFILEPATH = '/home/miahro/tiralabra/tiralabraknn/data' #pitää tehdä järkevämmin
