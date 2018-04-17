"""
This is the source file for the example spectrum. It has the dependencies of
using LaTeX with matplotlib. (See https://matplotlib.org/users/usetex.html) If
a LaTeX independent version is desired, simply comment out the line
plt.rc('text', usetex=True)
"""

import os
import re

import matplotlib.pyplot as plt

import lrspectrum


# Get multiple logfiles
lglst = []
for fil in os.listdir('.'):
    rexp = re.compile('example_\d.log')
    if rexp.match(fil) is not None:
        lglst.append(fil)

lr = lrspectrum.LRSpectrum(lglst)
lr.gen_spect(broad=1.0, wlim=(1530, 1570), res=200)

# Plotting options
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rc('xtick', top=True, direction='in')
plt.rc('xtick.major', size=4.5, pad=7)
plt.rc('xtick.minor', visible=True)
plt.rc('ytick', right=True, direction='in')
plt.rc('ytick.major', size=4.5)
plt.rc('ytick.minor', visible=True)

f, ax = plt.subplots(figsize=(4.25, 3.25))
lr.plot(ax=ax, xlim=(1555, 1575), xshift=23, ylabel='Intensity (Arb.)',
        xlabel='Energy (eV)', yscale=1000, sticks=False, ylim=(0, 3), ls='-',
        c='k', lw=1.5)
# Doing labels outside for fontsize
ax.set_xlabel('Energy (eV)', fontsize=14)
ax.set_ylabel('Intensity (Arb.)', fontsize=14)
'''
ax.set_xticklabels(['1555', '', '1556', '', '1557', '', '1558', '', '1559', '',
                    '1560', '', '1561', '', '1562', '', '1563', '', '1564', '',
                    '1565', '', '1566', '', '1567', '', '1568', '', '1569', '',
                    '1570']
                   ) 
'''
ax.set_xticklabels([str(i) for i in range(1555, 1571)])
ax.set_title('Calculated Aluminum K-Edge', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('aluminumKedge.png', dpi=500)
plt.show()
