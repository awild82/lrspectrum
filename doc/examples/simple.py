"""
This script is an example of the minimum needed (in a script) to use LRSpectrum

While many options are available for generating the spectrum, enough defaults
are assumed to allow for generation of the spectrum without any parameters.
For more info on the options available, look in lrspectrum.py or the other
example files.

lrspectrum must be installed (or a symbolic link to ../lrspectrum/lrspectrum.py
must be included in the calling directory)
"""

from lrspectrum import LRSpectrum

lr = LRSpectrum('example_ammonia.log')

# gen_spect must be called before plotting
lr.gen_spect()
# In order to see the plot, specify show=True
lr.plot(show=True)
