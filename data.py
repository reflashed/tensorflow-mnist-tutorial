import os
import gzip

to_dec = lambda x: int.from_bytes(x, byteorder='big')

def load_image_file(data_path):
    with gzip.open(data_path, 'r') as f:
        d = f.read()

    datum = {}

    num_images = to_dec(d[4:8])

    datum['magic_num'] = to_dec(d[:4]) # 3 dimensions in the vector / matrix
    datum['num_images'] = num_images 

    num_rows = to_dec(d[8:12])
    num_cols = to_dec(d[12:16])
    pixels = d[16:]

    datum['num_rows'] = num_rows
    datum['num_cols'] = num_cols

    images = []
    vec_len = num_rows * num_cols

    for i in range(0, num_images):
        start = vec_len * i
        vec = pixels[start:start+vec_len]
        images.append(vec)

    datum['images'] = images

    return datum

def load_label_file(data_path):
    with gzip.open(data_path, 'r') as f:
        d = f.read()

    datum = {}

    datum['magic_num'] = to_dec(d[:4]) # unsigned byte, 1 dimension in the vector / matrix
    datum['num_items'] = to_dec(d[4:8])

    labels = []
    labels_data = d[8:]

    for label_byte in labels_data:
        labels.append(int(label_byte))

    datum['labels'] = labels

    return datum

def load_mnist(data_dir):
    data = {
        'training': [],
        'test': []
    }

    files_data = {
        'training': ('train-labels-idx1-ubyte.gz', 'train-images-idx3-ubyte.gz'),
        'test': ('t10k-labels-idx1-ubyte.gz', 't10k-images-idx3-ubyte.gz')
    }

    for key in files_data.keys():
        files_datum = files_data[key]
        labels_file_name = files_datum[0]
        images_file_name = files_datum[1]

        labels_path = os.path.join(data_dir, labels_file_name)
        images_path = os.path.join(data_dir, images_file_name)

        labels_data = load_label_file(labels_path)
        images_data = load_image_file(images_path)

        for i in range(len(labels_data['labels'])):
            datum = {}
            datum['label'] = labels_data['labels'][i]
            datum['vector'] = images_data['images'][i]

            data[key].append(datum)

    return data
