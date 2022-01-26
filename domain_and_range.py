import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol, S, exp, log, pi, sqrt, sin, tan
from sympy.sets import Interval
from sympy.calculus.util import continuous_domain, function_range

x = Symbol('x')

#functions
a = sqrt(1 - x**2)
b = 1/x
c = sqrt(x)
d = sqrt(x**2 - 2)/x**2 - 1
e = 4/x**2
f = sqrt(x**2 - 1)
g = 3*x - sqrt(4 - 3*x)
h = sqrt(4 - x)
i = 3*x/sqrt(1 - x**3)
j = 1/(x + 2)
k = i + j

continuous_domain(d, x, S.Reals)

function_range(d, x, S.Reals)
