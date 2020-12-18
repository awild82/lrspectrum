import re


# TODO: Rewrite parsers to have a program specific root getter and a general
#       wrapper to ensure they each safely handle degenerate roots and do
#       necessary setup and returns

def _safe_add_or_extend(resdict, key, val):
    if key in resdict:
        resdict[key] += val
    else:
        resdict[key] = val


def _check_nonint(logfile):
    """Do not allow opening of files through file descriptors"""
    if isinstance(logfile, int):
        raise TypeError('Integer logfiles not allowed')


def detect(logfile):
    """ Automatically detects program that produced the logfile """

    # No file descriptor logfiles
    _check_nonint(logfile)

    fil = open(logfile)

    program = None
    # Not a super robust test, but likely sufficent
    for i in range(30):
        # Get new line
        try:
            line = next(fil)
        except StopIteration:
            break

        # Look for Gaussian (regular and gdv)
        if 'This is part of the Gaussian' in line:
            program = 'gaussian'
            break
        elif 'Gaussian' in line:
            program = 'gaussian'
            break
        elif 'ChronusQ' in line:
            program = 'chronus'
            break
        # Append additional programs here with elifs

    if program is None:
        program = 'delim'

    return program


def _parse_delim(logfile):
    """Parses a file delimited by characters outside the set [0-9e.-]"""

    # No file descriptor logfiles
    _check_nonint(logfile)

    results = {}
    fin = open(logfile)
    for line in fin:
        if 'excitation energy' in line.lower():
            if 'oscillator strength' in line.lower():
                line = line.strip()
                # Go until the numbers
                while len(re.split('[^0-9e.-]+', line)) != 2:
                    line = next(fin).strip()
                # Go until numbers stop
                while len(re.split('[^0-9e.-]+', line)) == 2:
                    lsp = re.split('[^0-9e.-]+', line)
                    _safe_add_or_extend(results, lsp[0], float(lsp[1]))
                    try:
                        line = next(fin).strip()
                    except StopIteration:
                        break
    return results


def _parse_gaussian(logfile):
    """Parses gaussian output"""

    # No file descriptor logfiles
    _check_nonint(logfile)

    results = {}
    for i, line in enumerate(open(logfile)):
        if 'Excited State' in line[1:14]:
            energy = line.split('eV')[0].strip().split()[-1]
            osstr = line.split('f')[1].strip().split('=')[1].strip().split()[0]
            # eV and unitless, respectively
            _safe_add_or_extend(results, energy, float(osstr))
    return results


def _parse_chronus(logfile):
    """Parses ChronusQ output"""

    # No file descriptors
    _check_nonint(logfile)

    results = {}
    fin = open(logfile)
    for i, line in enumerate(fin):
        if 'Root' in line:
            lsp = line.split()
            w = lsp[-1]
            line = next(fin)
            _safe_add_or_extend(results, w, float(line.split()[-1]))
    return results


def _parse_dummy(logfile):
    """Dummy parser for testing"""
    return {}


def _parse_test(logfile):
    """Parser that returns the same dict for testing"""
    return {'1': 1, '2': 1, '3': 2, '4': 3, '5': 5}


progs = {'gaussian': _parse_gaussian, 'chronus': _parse_chronus,
         'delim': _parse_delim, 'dummy': _parse_dummy, 'testing': _parse_test}
