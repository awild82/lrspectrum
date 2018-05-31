import os

import numpy as np
import pytest

from lrspectrum.parsers import detect
from lrspectrum.parsers import _parse_gaussian
from lrspectrum.parsers import _parse_delim


def check_same_dicts(dict1, dict2):
    assert len(dict1) == len(dict2)
    for (rk, rv), (ek, ev) in zip(dict1.items(), dict2.items()):
        print((rk, rv))
        print((ek, ev))
        assert rk == ek
        assert np.isclose(rv, ev)


def test_detect():
    """ Test parsers.detect """

    filname = '_test_detect.tmp'

    # Test custom errors
    with pytest.raises(TypeError):
        detect(0)

    # Test default
    fil = open(filname, 'w')
    fil.write('Blah blah blah')
    fil.close()
    expected = 'delim'
    result = detect(filname)
    assert expected == result

    # Test Gaussian detection
    fil = open(filname, 'w')
    fil.write('This is part of the Gaussian')
    fil.close()
    expected = 'gaussian'
    result = detect(filname)
    assert expected == result

    fil = open(filname, 'w')
    fil.write('Gaussian')
    fil.close()
    result = detect(filname)
    assert expected == result

    os.remove(filname)


def test__parse_gaussian():
    """ Test parsers._parse_gaussian """

    # Test custom errors
    with pytest.raises(TypeError):
        _parse_gaussian(0)

    # Test parsing
    filname = 'lrspectrum/test/data/single_root.log'
    expected = {'5.182': 0.3}
    result = _parse_gaussian(filname)
    check_same_dicts(expected, result)


def test__parse_delim():
    """" Test parsers._parse_delim """

    # Test custom errors
    with pytest.raises(TypeError):
        _parse_delim(0)

    # Test parsing
    filname = 'lrspectrum/test/data/delim0.txt'
    expected = {'12.568': 0.0213, '1.2789e3': 5.634e-5, '9.825': 10064.0}
    result = _parse_delim(filname)
    check_same_dicts(expected, result)

    filname = 'lrspectrum/test/data/delim1.txt'
    result = _parse_delim(filname)
    check_same_dicts(expected, result)
