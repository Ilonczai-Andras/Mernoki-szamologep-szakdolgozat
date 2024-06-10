import sympy as sp
from sympy import pprint, symbols
from sympy.stats import Poisson, density, E, variance, H, P

# Lambda paraméter meghatározása
lam = 5

# Poisson-eloszlás létrehozása
X = Poisson("X", lam)
x = symbols("x")

# Valószínűségi tömegfüggvény (PMF)
pmf = density(X)(x)

# Várható érték
mean = E(X)

# Variancia
var = variance(X)

# Entrópia
entropy = H(X)

print(P(X < 3))
print(pmf)
print(mean)
print(var)
print(entropy)
