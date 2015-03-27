# This will test whether or not FFTW FFTs can be repeatedly calculated
# in the same object, without needing to redeclare the empty array.
import numpy as np
import pyfftw

a = pyfftw.n_byte_align_empty((64, 64), 16, 'complex128')   # input
b = pyfftw.n_byte_align_empty((64, 64), 16, 'complex128')   # output
M = pyfftw.FFTW(a, b, axes=(0, 1))  # the FFT setup

# repeatedly calculate the FFT of a random matrix with M
for i in xrange(10):
    R = np.random.rand(64, 64)
    a[:, :] = R[:, :]
    M()

# check to see if the arrays are approximately equal
print np.allclose(np.fft.fft2(R), b)
