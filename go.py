import os

from data import load_mnist
from plot import show_im

DATA_DIR = os.path.join(os.getcwd(), 'data')
mnist = load_mnist(DATA_DIR)
show_im(mnist['training'][9])
