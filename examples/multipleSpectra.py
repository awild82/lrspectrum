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

#This is an example of generating one plot with multiple spectra

#lrspectrum.py or a symbolic link needs to be included in calling directory
from lrspectrum import LRSpectrum

#Multiple instances of LRSpectrum can be created with different logfiles
lr0 = LRSpectrum('ammonia','example_ammonia.log')
lr1 = LRSpectrum('formaldehyde','example_formaldehyde.log')
lr2 = LRSpectrum('methane','example_methane.log')

#Generating the spectra is the same as before
lr0.genSpect()
lr1.genSpect()
lr2.genSpect()

#Turn off roots with sticks=False
lr0.plot(sticks=False)
lr1.plot(sticks=False)
lr2.plot(sticks=False,show=True)

#Note that the default genSpect options aren't always good. We will look at
#  a way of accounting for this in a bit

#While the above works alright for small sets of logfiles, a better method can 
#  iterate through a list of LRSpectrum to minimize repeated code.
import os
import re

lrlst = []
rexp = re.compile('example_[^\W\d_]+.log')
for fil in os.listdir('.'):
    if rexp.match(fil) is not None:
        name = fil.split('.')[0].split('_')[1]
        lrlst.append(LRSpectrum(name,fil))
    
#Here we will determine a satisfactory option for wlim (limits on frequency
#  range) in genSpect
mn = min([min([float(k) for k in lr.roots.keys()]) for lr in lrlst])
mx = max([max([float(k) for k in lr.roots.keys()]) for lr in lrlst])
extra = (mx-mn)*0.5
mn -= extra
mx += extra
if mn < 0:
    mn = 0

#The above code attempts to automatically generate a range of frequencies
#It is often easier and produces better results simply to give a custom,
#  well defined wlim
#mn = 0
#mx = 20

for lr in lrlst:
    lr.genSpect(wlim=(mn,mx))
    if lr == lrlst[-1]:
        lr.plot(sticks=False,show=True)
    else:
        lr.plot(sticks=False)


