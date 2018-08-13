import sewpy as sp


a = "4.5-5"
b = 1.5e-5

sum = sp.getfloat(a) + b
print("{} + {} = {}".format(a, b, sum))
