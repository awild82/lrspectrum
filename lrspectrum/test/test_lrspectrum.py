import numpy as np
import pytest

from lrspectrum import LRSpectrum


def test_parse_log():
    """ Test LRSpectrum.parse_log """

    good_test = 'lrspectrum/test/data/example_methane.log'

    # Error checking
    lr = LRSpectrum(good_test, program='dummy')
    with pytest.raises(TypeError):
        lr.parse_log(program=0)
    with pytest.raises(ValueError):
        lr.parse_log(program='Fake program')

    # Check parser independent values
    lr.logfile = [good_test]
    lr.parse_log(program='testing')
    assert lr.roots == {'1': 1, '2': 1, '3': 2, '4': 3, '5': 5}

    # Finally, check that the update call correctly overlaps dicts
    lr.logfile = [good_test, good_test]
    lr.parse_log(program='testing')
    assert lr.roots == {'1': 1, '2': 1, '3': 2, '4': 3, '5': 5}


def test___init__():
    """ Test initialization of LRSpectrum """

    good_test = 'lrspectrum/test/data/example_methane.log'

    # Error checking
    with pytest.raises(TypeError):
        LRSpectrum(0)

    # Check initialized variables
    lr = LRSpectrum(good_test, program='dummy')
    assert lr.logfile == [good_test]
    assert lr.name is None
    assert lr.roots == {}
    assert lr.freq is None
    assert lr.spect is None
    assert lr.broad is None
    assert lr.wlim is None
    assert lr.res is None

    # Check initialization for passing a list
    lr = LRSpectrum([good_test]*2, program='dummy')
    assert lr.logfile == [good_test]*2


def test_gen_spect():
    """ Test LRSpectrum.gen_spect """

    single_root = 'lrspectrum/test/data/single_root.log'
    lr = LRSpectrum(single_root, program='Gaussian')
    lr.gen_spect(broad=0.5)

    # Test error raising
    # Test broad
    with pytest.raises(TypeError):
        lr.gen_spect(broad={'a': 0.5})
    # Test wlim
    with pytest.raises(TypeError):
        lr.gen_spect(wlim=1)
    with pytest.raises(TypeError):
        lr.gen_spect(wlim='a')
    with pytest.raises(IndexError):
        lr.gen_spect(wlim=[1])
    # Test res
    with pytest.raises(TypeError):
        lr.gen_spect(res='a')
    # Test meth
    with pytest.raises(TypeError):
        lr.gen_spect(meth=5)
    with pytest.raises(ValueError):
        lr.gen_spect(meth='ThIs iS nOt A sUpPoRtEd MeThOd')

    # Test automatic spectrum generation
    expected = np.array([2.9451285853942224, 7.418871414605778], dtype='float')
    actual = np.array([i for i in lr.wlim], dtype='float')
    assert np.allclose(expected, actual)

    # Test values
    wlim = (2.9451285853942224, 7.418871414605778)
    # Lorentzian
    expected = np.loadtxt('lrspectrum/test/data/single_root_spect.txt')
    lr.gen_spect(broad=0.5, wlim=wlim, res=100, meth='lorentz')
    assert np.allclose(lr.freq, expected[:, 0])
    assert np.allclose(lr.spect, expected[:, 1])
    # Gaussian
    expected = np.loadtxt('lrspectrum/test/data/single_root_gaussian.txt')
    lr.gen_spect(broad=0.5, wlim=wlim, res=100, meth='gaussian')
    assert np.allclose(lr.freq, expected[:, 0])
    assert np.allclose(lr.spect, expected[:, 1])

    # Test that a runtime error is raised when automatically generating
    # spectral range and all oscillator strengths are zero
    lr.roots = {}
    try:
        lr.gen_spect(broad=0.5)
        raise AssertionError(
            "Did not raise Runtime Error when determining wlim in " +
            "gen_spect() with no roots")  # pragma: no cover
    except RuntimeError:
        pass


def test__gaussian():
    """ Test generation of gaussian distribution """
    # Because this is a hidden method, it is not meant to be called directly,
    # and type checking is not performed

    # Test values
    single_root = 'lrspectrum/test/data/single_root.log'
    lr = LRSpectrum(single_root, program='Gaussian')
    lr.freq = np.array([0])
    # Un-normalized (0,1) gaussian should be 1 at x=0
    result = lr._gaussian(np.sqrt(2.0*np.log(2.0)), 0, 1)*np.sqrt(2*np.pi)
    assert np.allclose(np.ones((1,)), result)
    # Test non-zero, normalized and scaled
    lr.freq = np.array([1.5])
    expected = np.array([0.02330233])
    result = lr._gaussian(np.sqrt(2.0*np.log(2.0)), 0.3, 0.12)
    assert np.allclose(expected, result)


def test__lorentz():
    """ Test generation of lorentzian distribution """
    # Because this is a hidden method, it is not meant to be called directly,
    # and type checking is not performed

    # Test values
    single_root = 'lrspectrum/test/data/single_root.log'
    lr = LRSpectrum(single_root, program='Gaussian')
    lr.freq = np.array([0])
    # Un-normalized (0,1) lorentz should be 1 at x=0
    result = lr._lorentz(1, 0, 1)*np.pi
    assert np.allclose(np.ones((1,)), result)
    # Test non-zero, normalized and scaled
    lr.freq = np.array([1.5])
    expected = np.array([0.01565458])
    result = lr._lorentz(1, 0.3, 0.12)
    assert np.allclose(expected, result)


def test_plot():
    """ Test LRSpectrum.plot internals """
    # Because most of the arguments are passed to pyplot, the error checking is
    # handled there. We only check the arguments we use to shift and scale

    # Test exceptions
    single_root = 'lrspectrum/test/data/single_root.log'
    lr = LRSpectrum(single_root, program='Gaussian')
    # x options
    with pytest.raises(TypeError):
        lr.plot(do_spect=False, show=False, xscale='a')
    with pytest.raises(TypeError):
        lr.plot(do_spect=False, show=False, xshift='a')
    with pytest.raises(TypeError):
        lr.plot(do_spect=False, show=False, xlim=123)
    with pytest.raises(IndexError):
        lr.plot(do_spect=False, show=False, xlim=[1])
    with pytest.raises(TypeError):
        lr.plot(do_spect=False, show=False, xlim=(1, 'b'))
    # y options
    with pytest.raises(TypeError):
        lr.plot(do_spect=False, show=False, yscale='a')
    with pytest.raises(TypeError):
        lr.plot(do_spect=False, show=False, yshift='a')
    with pytest.raises(TypeError):
        lr.plot(do_spect=False, show=False, ylim=123)
    with pytest.raises(IndexError):
        lr.plot(do_spect=False, show=False, ylim=[1])
    with pytest.raises(TypeError):
        lr.plot(do_spect=False, show=False, ylim=(1, 'b'))
    # Returns None when calling with no spectrum
    result = lr.plot(do_spect=True, show=False)
    assert result is None

    # Test values
    lr.freq = np.array([2, 4, 5, 6, 9])
    lr.spect = np.array([0, 1, 2, 3, 4])
    xlim = (0, 10)
    ylim = (-1, 5)
    xshift = 5.3
    xscale = 0.5
    yscale = 2.1
    yshift = 3.9
    exlim = tuple([x*xscale + xshift for x in xlim])
    eylim = tuple([y*yscale + yshift for y in ylim])
    expect_freq = lr.freq*xscale + xshift
    exspected = lr.spect*yscale + yshift
    # Test modified xlim/ylim and values
    ax = lr.plot(do_spect=True, show=False, xshift=xshift, yshift=yshift,
                 xscale=xscale, yscale=yscale, xlim=xlim, ylim=ylim)
    assert np.allclose(exlim, ax.get_xlim())
    assert np.allclose(eylim, ax.get_ylim())
    assert np.allclose(expect_freq, ax.lines[0].get_xdata())
    assert np.allclose(exspected, ax.lines[0].get_ydata())
