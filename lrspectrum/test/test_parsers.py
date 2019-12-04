import os

import numpy as np
import pytest

from lrspectrum.parsers import detect
from lrspectrum.parsers import _safe_add_or_extend
from lrspectrum.parsers import _parse_gaussian
from lrspectrum.parsers import _parse_chronus
from lrspectrum.parsers import _parse_delim


def check_same_dicts(dict1, dict2):
    assert len(dict1) == len(dict2)
    for (key, val) in dict1.items():
        print(key, val)
        assert key in dict2.keys()
        assert np.isclose(val, dict2[key])


def test__safe_add_or_extend():
    expect = {'a': 1.0, 'b': 12.0}
    res = {'b': 9.5}
    _safe_add_or_extend(res, 'a', 1.0)
    _safe_add_or_extend(res, 'b', 2.5)
    check_same_dicts(expect, res)


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

    # Test ChronusQ detection
    fil = open(filname, 'w')
    fil.write('ChronusQ')
    fil.close()
    expected = 'chronus'
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

    # Test degenerate roots
    filname = 'lrspectrum/test/data/degenerate_gaussian.log'
    result = _parse_gaussian(filname)
    assert np.allclose(result['388.9345'], 0.1663)


def test__parse_chronus():
    """ Test parsers._parse_chronus """

    with pytest.raises(TypeError):
        _parse_chronus(0)

    # Test parsing
    filname = 'lrspectrum/test/data/chronusq.out'
    expected = {'0.92663078': 0.0001608,
                '1.79614206': 0.00923395,
                '1.82439203': 0.01562033}
    result = _parse_chronus(filname)
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
