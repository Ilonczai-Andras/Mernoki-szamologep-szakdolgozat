from sympy.stats import Normal, P, E, variance
from sympy import symbols

# Definiáljuk a normál eloszlású változót
mu = 10
sigma = 2
X = Normal('X', mu, sigma)

# Várható érték (átlag)
expected_value = E(X)
print(f"Várható érték: {expected_value}")

# Variancia
var = variance(X)
print(f"Variancia: {var}")

# Valószínűség számítása, hogy X kisebb mint 12
prob = P(X < 12)
print(f"P(X < 12) = {prob}")
