
import time
import random
import json
import numpy as np
import os, sys
from PIL import Image
import matplotlib.pyplot as plt

TAB = "    "

def write(fname, s):
    with open(fname, 'w') as f:
        f.write(s)
        
def read(fname):
    with open(fname) as f:
        return f.read()

def file_name(fname, ext):
    x = fname.split('.')[0]
    x += '.' + ext
    return x

def quickname(ext='txt'):
    v = str(time.time()).split('.')
    s = f"file{v[0]}{v[1]}.{ext}"
    return s

def create_random_image(fname = 'image.jpg',
                       height = 100,
                       width = 100,
                       depth = 3):
    x = np.random.uniform(0, 1,
                          size = (height, width, depth))
    plt.imsave(fname, x)
    return fname
    

def txt_to_py(txtname, pyname=None):
    '''Creates a .py file based on a .txt file
    Returns string representing name of the .py file
    @param txtname : string, Name of.txt file in this directory
    @param pyname : string, name of .py file you want to create
    '''
    if not pyname:
        pyname = file_name(txtname, ext = 'py')
    x = read(txtname)
    write(pyname, x)
    return pyname

def txt_to_py_list(el):
    ret = []
    for x in el:
        ret.append(txt_to_py(x))
    return ret

def execfile(pyname):
    s = f'python3 {pyname}'
    return os.system(s)

