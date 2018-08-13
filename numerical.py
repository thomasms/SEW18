def getfloat(value):
    """
        Gets the floating point value from a string
        Will allow for fortran style floats, i.e -2.34321-308
        If it is neither then it will return "nan"
    """
    if istraditionalfloat(value):
        return float(value)

    return getfortranfloat(value)


def istraditionalfloat(value):
    """
        Checks if the string can be converted to a floating point value
        Does not allow for fortran style floats, i.e -2.34321-308
        only standard floats.
    """
    try:
        float(value)
        return True
    except ValueError:
        return False

def isfloat(value):
    """
        Checks if the string can be converted to a floating point value
        Will allow for fortran style floats, i.e -2.34321-308
        If it is neither then it will return False
    """
    if isinstance(value, (int, float, str)):
        return istraditionalfloat(value) or isfortranfloat(value)
    return False

def isfortranfloat(value):
    passfunc = lambda sign, esign, parts: True
    failfunc = lambda: False

    return _fortranfloat(value, passfunc, failfunc)


def getfortranfloat(value):
    passfunc = lambda sign, esign, parts: float(sign + parts[0] + 'E' + esign + parts[1])
    failfunc = lambda: "nan"

    return _fortranfloat(value, passfunc, failfunc)


def _fortranfloat(value, passfunc, failfunc):
    # could be 2.3
    #          2.3e+10
    #          -2.3e+10
    #          -2.3+10
    #          -2.3-10
    #          2.3-10
    #          +2.3-10
    #          +2.3+10
    #          -2.3+10

    signs = ['-', '+']

    valueasstring = str(value)
    sign = ""
    if valueasstring:
        # check for sign at the front
        if valueasstring[0] in signs:
            sign = valueasstring[0]
            valueasstring = valueasstring[1:]

        # cannot have both separators in the value for a valid float
        if not all(s in valueasstring for s in signs):
            # check the values in both parts recursively
            for sn in signs:
                if sn in valueasstring:
                    parts = valueasstring.split(sn, 1)
                    if istraditionalfloat(parts[0]) and \
                       istraditionalfloat(parts[1]) and \
                       '.' in parts[0] and '.' not in parts[1]:
                        return passfunc(sign, sn, parts)
    return failfunc()
