import sympy as sp

a = sp.Matrix([
    [1, 2, -3, 0],
    [2, 4, -2, 2],
    [3, 6, -4, 3]
])

a.echelon_form()
