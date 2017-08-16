"""
Copyright 2017 Andrew Wildman

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

#This is an example of generating a single spectrum over several log files
#This may be convienent when trying to solve for a large number states in
#a dense region of the spectrum (like XAS, for example)

#lrspectrum.py or a symbolic link to it needs to be in the calling directory
from lrspectrum import LRSpectrum

#LRSpectrum supports logfiles listed as multiple params
lr0 = LRSpectrum('LogParams','example_1.log','example_2.log','example_3.log')

#or as a list of logfiles.
logs = ['example_1.log','example_2.log','example_3.log']
lr1  = LRSpectrum('LogList',logs)

#The second is particularly convenient when your log files are systematically
#  named. One option to take advantage of this is as follows.
lglst = []
#Best practice is to include all imports at the beginning of the script. Here,
#we deviate in order to make clear which portions are dependent on which modules
import os
import re
for fil in os.listdir('.'):
    rexp = re.compile('example_\d.log')
    if rexp.match(fil) is not None:
        lglst.append(fil)

lr2 = LRSpectrum('RELogs',lglst)

#All methods provide the same spectrum
lr0.genSpect()
lr1.genSpect()
lr2.genSpect()

import matplotlib.pyplot as plt
#You can specify which axis to plot on with ax
f, axs = plt.subplots(nrows=3,sharex=True)
lr0.plot(ax=axs[0],xLabel=None)
lr1.plot(ax=axs[1],xLabel=None)
lr2.plot(ax=axs[2],show=True)

