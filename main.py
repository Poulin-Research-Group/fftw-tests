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
print 'constructed random matrices'

# matrices for pyfftw
n1_in  = pyfftw.n_byte_align_empty((64, 64), 16, 'complex128')
n1_out = pyfftw.n_byte_align_empty((64, 64), 16, 'complex128')
N1 = pyfftw.FFTW(n1_in, n1_out, axes=(0, 1))
n1_in[:, :] = M1[:, :]

n2_in  = pyfftw.n_byte_align_empty((128, 128), 16, 'complex128')
n2_out = pyfftw.n_byte_align_empty((128, 128), 16, 'complex128')
N2 = pyfftw.FFTW(n2_in, n2_out, axes=(0, 1))
n2_in[:, :] = M2[:, :]

n3_in  = pyfftw.n_byte_align_empty((256, 256), 16, 'complex128')
n3_out = pyfftw.n_byte_align_empty((256, 256), 16, 'complex128')
N3 = pyfftw.FFTW(n3_in, n3_out, axes=(0, 1))
n3_in[:, :] = M3[:, :]

n4_in  = pyfftw.n_byte_align_empty((512, 512), 16, 'complex128')
n4_out = pyfftw.n_byte_align_empty((512, 512), 16, 'complex128')
N4 = pyfftw.FFTW(n4_in, n4_out, axes=(0, 1))
n4_in[:, :] = M4[:, :]

n5_in  = pyfftw.n_byte_align_empty((1024, 1024), 16, 'complex128')
n5_out = pyfftw.n_byte_align_empty((1024, 1024), 16, 'complex128')
N5 = pyfftw.FFTW(n5_in, n5_out, axes=(0, 1))
n5_in[:, :] = M5[:, :]

n6_in  = pyfftw.n_byte_align_empty((2048, 2048), 16, 'complex128')
n6_out = pyfftw.n_byte_align_empty((2048, 2048), 16, 'complex128')
N6 = pyfftw.FFTW(n6_in, n6_out, axes=(0, 1))
n6_in[:, :] = M6[:, :]

n7_in  = pyfftw.n_byte_align_empty((4096, 4096), 16, 'complex128')
n7_out = pyfftw.n_byte_align_empty((4096, 4096), 16, 'complex128')
N7 = pyfftw.FFTW(n7_in, n7_out, axes=(0, 1))
n7_in[:, :] = M7[:, :]

n8_in  = pyfftw.n_byte_align_empty((8192, 8192), 16, 'complex128')
n8_out = pyfftw.n_byte_align_empty((8192, 8192), 16, 'complex128')
N8 = pyfftw.FFTW(n8_in, n8_out, axes=(0, 1))
n8_in[:, :] = M8[:, :]
print 'built pyfftw matrices\n'


def pyfftw_test(A):
    result = A()


def numpy_test(A):
    result = np.fft.fft2(A)


num = 10
for M, N in zip([M1, M2, M3, M4, M5, M6, M7, M8], [N1, N2, N3, N4, N5, N6, N7, N8]):
    numpy_timer  = timeit.Timer("numpy_test(M)",  "from __main__ import M, numpy_test")
    pyfftw_timer = timeit.Timer("pyfftw_test(N)", "from __main__ import N, pyfftw_test")
    print "shape:", M.shape, num, "trials"

    numpy_time  = numpy_timer.timeit(number=num)
    pyfftw_time = pyfftw_timer.timeit(number=num)
    print "  ",  numpy_time,  "seconds"
    print "  ",  pyfftw_time, "seconds"
    print "  pyfftw is", (numpy_time/pyfftw_time), "times faster\n"
