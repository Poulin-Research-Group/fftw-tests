import pyfftw
import numpy as np
import timeit

# matrices for numpy
M1 = np.random.rand(64, 64) + np.random.rand(64, 64)*1j
M2 = np.random.rand(128, 128)   + np.random.rand(128, 128)*1j
M3 = np.random.rand(256, 256)   + np.random.rand(256, 256)*1j
M4 = np.random.rand(512, 512)   + np.random.rand(512, 512)*1j
M5 = np.random.rand(1024, 1024) + np.random.rand(1024, 1024)*1j
M6 = np.random.rand(2048, 2048) + np.random.rand(2048, 2048)*1j
M7 = np.random.rand(4096, 4096) + np.random.rand(4096, 4096)*1j
M8 = np.random.rand(8192, 8192) + np.random.rand(8192, 8192)*1j

# matrices for pyfftw
n1 = pyfftw.n_byte_align_empty((64, 64), 16, 'complex128')
n1[:, :] = M1[:, :]
N1 = pyfftw.builders.fft(n1)

n2 = pyfftw.n_byte_align_empty((128, 128), 16, 'complex128')
n2[:, :] = M2[:, :]
N2 = pyfftw.builders.fft(n2)

n3 = pyfftw.n_byte_align_empty((256, 256), 16, 'complex128')
n3[:, :] = M3[:, :]
N3 = pyfftw.builders.fft(n3)

n4 = pyfftw.n_byte_align_empty((512, 512), 16, 'complex128')
n4[:, :] = M4[:, :]
N4 = pyfftw.builders.fft(n4)

n5 = pyfftw.n_byte_align_empty((1024, 1024), 16, 'complex128')
n5[:, :] = M5[:, :]
N5 = pyfftw.builders.fft(n5)

n6 = pyfftw.n_byte_align_empty((2048, 2048), 16, 'complex128')
n6[:, :] = M6[:, :]
N6 = pyfftw.builders.fft(n6)

n7 = pyfftw.n_byte_align_empty((4096, 4096), 16, 'complex128')
n7[:, :] = M7[:, :]
N7 = pyfftw.builders.fft(n7)

n8 = pyfftw.n_byte_align_empty((8192, 8192), 16, 'complex128')
n8[:, :] = M8[:, :]
N8 = pyfftw.builders.fft(n8)


def pyfftw_test(A):
    result = A()


def numpy_test(A):
    result = np.fft.fft2(A)


num = 10
for M, N in zip([M1, M2, M3, M4, M5, M6, M7, M8], [N1, N2, N3, N4, N5, N6, N7, N8]):
    numpy_timer  = timeit.Timer("numpy_test(M)",  "from __main__ import M, numpy_test")
    pyfftw_timer = timeit.Timer("pyfftw_test(N)", "from __main__ import N, pyfftw_test")
    print "shape: ", M.shape, num, " trials"
    print "  ",  numpy_timer.timeit(number=num), "seconds"
    print "  ", pyfftw_timer.timeit(number=num), "seconds\n"
