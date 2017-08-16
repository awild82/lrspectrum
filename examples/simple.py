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

#This script is an example of the minimum needed (in a script) to use LRSpectrum

#Note that you need lrspectrum.py or a symbolic link to it in the directory from
#which this script is called
from lrspectrum import LRSpectrum

#If your lrspectrum.py is in the same directory as this script, comment out the
#lines above and uncomment the one below

#from lrspectrum import LRSpectrum

lr = LRSpectrum('Ammonia spectrum','example_ammonia.log')

"""
While many options are available for generating the spectrum, enough defaults
are assumed to allow for generation of the spectrum without any parameters.
For more info on the options available, look in lrspectrum.py or the other 
example files.
"""
#genSpect must be called before plotting
lr.genSpect()
#In order to see the plot, specify show=True
lr.plot(show=True)
