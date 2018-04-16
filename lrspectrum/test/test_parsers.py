import os

import pytest

from lrspectrum.parsers import detect
from lrspectrum.parsers import _parse_gaussian


def test_detect():
    """ Test parsers.detect """

    filname = '_test_detect.tmp'

    # Test custom errors
    with pytest.raises(TypeError):
        detect(0)

    with pytest.raises(RuntimeError):
        fil = open(filname, 'w')
        fil.write('This is not a known format')
        fil.close()
        detect(filname)

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
    for (rk, rv), (ek, ev) in zip(result.items(), expected.items()):
        assert rk == ek
        assert rv == ev
