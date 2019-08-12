import bz2

filename = 'model-tiny.h5.bz2'

compressed_path = filename
weight_path = 'model-tiny.h5'

# open and unzip file
with bz2.BZ2File(compressed_path, 'rb') as source:
    with open(weight_path, 'wb') as target:
        target.write(source.read())

import h5py
filename = 'model-tiny.h5'
f = h5py.File(filename, 'r')

print(f.keys())

print(f['classifier']['classifier_3']['bias:0'].value)