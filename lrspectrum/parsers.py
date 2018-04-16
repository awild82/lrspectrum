def detect(logfile):
    """ Automatically detects program that produced the logfile """

    # Do not allow opening of files through file descriptors
    if isinstance(logfile, int):
        raise TypeError('Integer logfiles not allowed')

    fil = open(logfile)

    program = None
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
        # Append additional programs here with elifs

    if program is None:
        raise RuntimeError(
            'Could not determine program for logfile {0}'.format(logfile)
        )

    return program


def _parse_gaussian(logfile):
    """ Parses gaussian output """

    # Do not allow opening of files through file descriptors
    if isinstance(logfile, int):
        raise TypeError('Integer logfiles not allowed')

    results = {}
    for i, line in enumerate(open(logfile)):
        if 'Excited State' in line[1:14]:
            lsp = line.split()
            results[lsp[4]] = float(lsp[8].lstrip('f='))
            # eV and unitless, respectively
    return results


def _parse_dummy(logfile):
    """ Dummy parser for testing """
    return {}


def _parse_test(logfile):
    """ Parser that returns the same dict for testing """
    return {'1': 1, '2': 1, '3': 2, '4': 3, '5': 5}


progs = {'gaussian': _parse_gaussian, 'dummy': _parse_dummy,
         'testing': _parse_test}
