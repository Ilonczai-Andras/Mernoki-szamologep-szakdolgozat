import sympy as sp
from sympy import pprint, symbols
from sympy.stats import Poisson, density, E, variance, H

# Lambda paraméter meghatározása
lam = 50

# Poisson-eloszlás létrehozása
X = Poisson('X', lam)
x = symbols('x')

# Valószínűségi tömegfüggvény (PMF)
pmf = density(X)(x)

# Várható érték
mean = E(X)

# Variancia
var = variance(X)

# Entrópia
entropy = H(X)

print(pmf)
print(mean)
print(var)
print(entropy)
