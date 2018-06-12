# LRSpectrum

A utility for parsing and plotting spectra from linear response calculations 

[![Build Status](https://travis-ci.org/awild82/lrspectrum.svg?branch=master)](https://travis-ci.org/awild82/lrspectrum)
[![Coverage Status](https://coveralls.io/repos/github/awild82/lrspectrum/badge.svg?branch=master)](https://coveralls.io/github/awild82/lrspectrum?branch=master)

<p align="center">
<img src="./doc/media/aluminumKedge.png" alt="Example Spectrum" width="500px"/>
</p>

## Easy start

First, get the repo:

`$ git clone https://github.com/awild82/lrspectrum.git`

Install using setuptools:

`$ python setup.py install --user`

To plot, you have two options. The easier of the two uses all the default
options, so it is not recommended for final figures. After installing, navigate
to the directory with your log files, then

`$ python -m lrspectrum <logfile> [<logfile> ...]`

This allows for plotting one spectrum that was generated across one or more
logfiles.

The second options is to write a basic python script and run it. All you need to
do is specify the log file, generate the spectrum, and call the plot method:
```
import lrspectrum

logfile = 'xyz/logfile.log'

lr = lrspectrum.LRSpectrum(logfile)
lr.gen_spect()
lr.plot(show=True)
```

Run this file with

`$ python <filename>`

This is the bare bones configuration. For more customizability, see the sections
below!

## Installation

LRSpectrum currently supports installation after cloning the github repository.
Future development aims to put it on PyPI, but is currently unavailable.

### Dependencies

Core Dependencies:
 * numpy
 * matplotlib

Testing Dependencies:
 * pytest
 * pytest-cov

The easiest way to install all the dependencies is to run
`$ pip install -r requirements.txt`

### Instructions

Once you have all the dependencies, clone the repo:
`$ git clone https://github.com/awild82/lrspectrum.git`

`setup.py` can be run the following ways:
 1. `$ python setup.py install --user`
 2. `$ ./setup.py install --user`
 3. `$ python3 setup.py install --user`
 4. `$ python2 setup.py install --user`

The first option should work regardless of platform, and is the recommended
installation option.

The second option assumes you have a python interpreter installed at
`/bin/python`. The module will be installed on that interpreter.

The third and fourth options are for python 3 or 2 specific installations.

Of course, if a system-wide installation is desired, omit the `--user` flag from
the previous instructions. 

## Testing

Simply run
`$ make test`
or
`$ python -m pytest --pyargs lrspectrum --cov-report term-missing --cov=lrspectrm`

## Contributing

Found a bug? Please report it in the issues!

Want to add a feature or get involved in development? Great! Please see
[contributing.md](./doc/contributing.md).

## License

lrspectrum is licensed under the MIT license. See [LICENSE](./LICENSE) for more 
details.
