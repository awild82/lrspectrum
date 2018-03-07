import sys

from . import lrspectrum


lr = lrspectrum.LRSpectrum(sys.argv[1:])
lr.gen_spect()
lr.plot(show=True)
