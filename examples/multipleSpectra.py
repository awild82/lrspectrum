"""
This is an example of generating one plot with multiple spectra

lrspectrum must be installed (or a symbolic link to ../lrspectrum/lrspectrum.py
must be included in the calling directory)
"""
import os
import re

from lrspectrum import LRSpectrum

# Multiple instances of LRSpectrum can be created with different logfiles
lr0 = LRSpectrum('example_ammonia.log', name='ammonia')
lr1 = LRSpectrum('example_formaldehyde.log', name='formaldehyde')
lr2 = LRSpectrum('example_methane.log', name='methane')

# Generating the spectra is the same as before
lr0.gen_spect()
lr1.gen_spect()
lr2.gen_spect()

# Turn off roots with sticks=False
lr0.plot(sticks=False)
lr1.plot(sticks=False)
lr2.plot(sticks=False, show=True)

# Note that the default gen_spect options aren't always good. We will look at
# a way of accounting for this in a bit

# While the above works alright for small sets of logfiles, a better method can
# iterate through a list of LRSpectrum to minimize repeated code.

lrlst = []
rexp = re.compile('example_[^\W\d_]+.log')
for fil in os.listdir('.'):
    if rexp.match(fil) is not None:
        name = fil.split('.')[0].split('_')[1]
        lrlst.append(LRSpectrum(fil, name=name))

# Here we will determine a satisfactory option for wlim (limits on frequency
# range) in gen_spect
mn = min([min([float(k) for k in lr.roots.keys()]) for lr in lrlst])
mx = max([max([float(k) for k in lr.roots.keys()]) for lr in lrlst])
extra = (mx-mn)*0.5
mn -= extra
mx += extra
if mn < 0:
    mn = 0

# The above code attempts to automatically generate a range of frequencies
# It is often easier and produces better results simply to give a custom,
# well defined wlim
# mn = 0
# mx = 20

for lr in lrlst:
    lr.gen_spect(wlim=(mn, mx))
    if lr == lrlst[-1]:
        lr.plot(sticks=False, show=True)
    else:
        lr.plot(sticks=False)
