from sympy import symbols, diff, integrate, sin

# Szimbolikus változók definiálása
x, y = symbols('x y')

# Példa egy egyszerű függvény definiálására és deriválására
f = x**2 + 3*x + 2
f_derivative = diff(f, x)
print("Függvény: ", f)
print("Függvény deriváltja: ", f_derivative)

# Példa integrálásra
integral = integrate(f, x)
print("Függvény integrálja: ", integral)

# Példa szinuszfüggvény integrálására
sin_integral = integrate(sin(x), x)
print("Sinus függvény integrálja: ", sin_integral)
