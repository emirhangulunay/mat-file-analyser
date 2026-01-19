from os.path import dirname, join as pjoin
import scipy.io as sio
import numpy as np


data_dir = pjoin(dirname(sio.__file__), 'matlab', 'tests', 'data')
mat_fname = pjoin(data_dir, 'testdouble_7.4_GLNX86.mat')

mat_contents = sio.loadmat(mat_fname, spmatrix=False)

matstruct_fname = pjoin(data_dir, 'teststruct_7.4_GLNX86.mat')
matstruct_contents = sio.loadmat(matstruct_fname)
teststruct = matstruct_contents['teststruct']
teststruct.dtype


matstruct_squeezed = sio.loadmat(matstruct_fname, squeeze_me=True)
matstruct_squeezed['teststruct'].shape
()
matstruct_squeezed['teststruct']['complexfield'].shape
()
matstruct_squeezed['teststruct']['complexfield'].item()
np.array([ 1.41421356+1.41421356j,  2.71828183+2.71828183j, 
       3.14159265+3.14159265j])
