"""
This is an example of generating a single spectrum over several log files
This may be convienent when trying to solve for a large number states in
a dense region of the spectrum (like XAS, for example)

lrspectrum must be installed (or a symbolic link to ../lrspectrum/lrspectrum.py
must be included in the calling directory)
"""
import os
import re

import matplotlib.pyplot as plt

from lrspectrum import LRSpectrum


# LRSpectrum supports logfiles listed as multiple params
lr0 = LRSpectrum('example_0.log', 'example_1.log', 'example_2.log',
                 name='LogParams')

# Or as a list of logfiles.
logs = ['example_0.log', 'example_1.log', 'example_2.log']
lr1 = LRSpectrum(logs, name='LogList')

# The second is particularly convenient when your log files are systematically
# named. One option to take advantage of this is as follows.

lglst = []
for fil in os.listdir('.'):
    rexp = re.compile('example_\d.log')
    if rexp.match(fil) is not None:
        lglst.append(fil)

lr2 = LRSpectrum(lglst, name='RELogs')

# All methods provide the same spectrum
lr0.gen_spect()
lr1.gen_spect()
lr2.gen_spect()

# You can specify which axis to plot on with ax
f, axs = plt.subplots(nrows=3, sharex=True)
lr0.plot(ax=axs[0], xLabel=None)
lr1.plot(ax=axs[1], xLabel=None)
lr2.plot(ax=axs[2], show=True)
