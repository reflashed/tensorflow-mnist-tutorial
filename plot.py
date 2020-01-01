import numpy as np
import matplotlib.pyplot as plt

def show_im(datum):
    label = datum['label']
    vec = datum['vector']

    arr = []
    for byte in vec:
        arr.append(int(byte))

    px = np.array(arr, dtype='uint8')
    px = px.reshape((28, 28))

    plt.title('Label is {}'.format(label))
    plt.imshow(px, cmap='gray')
    plt.show()
