from sympy.stats import Pareto, entropy, density, E, variance, P, entropy
from sympy import Symbol, S, sympify, gamma, log, digamma

x = Symbol("x")

xm = 1
alpha = 3
X = Pareto("X", xm, alpha)

print("sűrűség fgv:", density(X)(x))
print("várható ért: ", E(X).evalf())
print("variancia: ", variance(X).evalf())
print("entrópia: ", entropy(X).evalf())
condition = sympify("X < 3", locals={"X": X})
print("valség: ", str(P(condition).evalf()))
