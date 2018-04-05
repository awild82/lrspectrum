def detect(logfile):
    """ Automatically detects program that produced the logfile """
    if not isinstance(logfile, str):
        raise TypeError(
            'Expected string for input "logfile". ' +
            'Recieved {0}'.format(type(logfile))
        )
    fil = open(logfile)
    program = None
    for i in range(30):
        line = next(fil)
        if 'This is part of the Gaussian' in line:
            program = 'gaussian'
            break
        elif 'Gaussian' in line:
            program = 'gaussian'
            break
    if program is None:
        raise RuntimeError(
            'Could not determine program for logfile {0}'.format(logfile)
        )
    return program


def _parse_gaussian(logfile):
    """ Parses gaussian output """
    results = {}
    for i, line in enumerate(open(logfile)):
        if 'Excited State' in line[1:14]:
            lsp = line.split()
            results[lsp[4]] = float(lsp[8].lstrip('f='))
            # eV and unitless, respectively
    return results


progs = {'gaussian': _parse_gaussian}
