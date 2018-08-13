import sewpy as sp


value = "4.5-95"


if sp.isfloat(value):
    print("{} is a float equivalent to {}".format(value, sp.getfloat(value)))
else:
    print("{} is not a float".format(value))
