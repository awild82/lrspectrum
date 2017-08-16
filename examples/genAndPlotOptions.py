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

#This is a script that demonstrates the variety of generation and plotting
#  options available through LRSpectrum

#lrspectrum.py or a symbolic link must be included in the calling directory
from lrspectrum import LRSpectrum
import matplotlib.pyplot as plt
import numpy as np

lr = LRSpectrum('Ammonia','example_ammonia.log')

"""
The default options for genSpect choose a fairly standard broadening level,
  attempt to automatically define an appropriate frequency range, and assume
  that a lorentzian lineshape is desired. All of these options can be manually 
  specified.
"""

#--------------------------------------------------------------------------
# Broadening parameters
#--------------------------------------------------------------------------

wlim  = (0,20) #Frequency range in eV
#Here we define a list of broadening levels so we can plot them
broad = [0.1, 0.2, 0.5, 0.8, 1.5]

#Keeping lorentzian and default resolution for now
for b in broad:
    lr.genSpect(wlim=wlim,broad=b)
    #Do not plot roots (sticks=False)
    lr.plot(sticks=False)

plt.legend(broad)

#Add sticks then show all
lr.plot(doSpect=False,show=True)


#--------------------------------------------------------------------------
# Lorentzian versus gaussian lineshape
#--------------------------------------------------------------------------

lr.genSpect(wlim=wlim)
lr.plot(sticks=False)

lr.genSpect(wlim=wlim,meth='gaussian')
lr.plot()

plt.legend(['Lorentzian','Gaussian'])
plt.show()

#--------------------------------------------------------------------------
# Increasing resolution 
#--------------------------------------------------------------------------

res = [5, 10, 20, 50, 100, 500, 1000]

for r in res:
    lr.genSpect(wlim=wlim,res=r)
    lr.plot(sticks=False)

plt.legend(res)
#xlim and ylim set limits on the plotting axes
lr.plot(xlim=(6,7.5),ylim=(0,0.05),doSpect=False,show=True)

#--------------------------------------------------------------------------
# Default plotting options 
#--------------------------------------------------------------------------

"""
We have already seen doSpect, sticks, and show. The other options are:
    xLabel:  Label on x-axis;                  Default='Energy / eV'
    yLabel:  Label on y-axis;                  Default='Arbitrary Units'
    ax:      Axis on which to place the plot;  Default=Current axes

For example, if we were to want to plot the spectrum in nm rather than eV,
(although integration of this feature is planned) we could do: 
"""

fig, axs = plt.subplots(ncols=2,sharey=True)
lr.genSpect(wlim=(0.001,15))
lr.plot(ax=axs[0])
#While this works, it seems like bad practice, since it may break things
#  that assume lr.freq is in eV. For now, this is included because it 
#  allows for showcasing xLabel, yLabel, and ax

#Constant is h*c in eV*nm
lr.freq = np.divide(1239.842*np.ones(lr.freq.shape),lr.freq)
lr.plot(ax=axs[1],yLabel=None,xLabel='Wavelength (nm)',xlim=(50,300),
        sticks=False,show=True)

#--------------------------------------------------------------------------
# Using matplotlib.pyplot options
#--------------------------------------------------------------------------

"""
In addition to the explicit plotting options given as arguments, any other
matplotlib.pyplot options can be passed into LRSpectrum.plot. This is useful
for changing formatting.
"""

lr.genSpect(wlim=wlim)
lr.plot(sticks=False,lw=2,color='r',ls='--')
lr.plot(doSpect=False,lw=2,color='b',ls=':',show=True)




