import numpy as np
import matplotlib.pyplot as plt

# Define the expression
x = np.linspace(0.1, 3*np.pi, 1000)  # Restricting x to avoid complex values
expression = -np.log10(np.sin(x) - 1)/2 + np.log10(np.sin(x) + 1)/2

# Plot the expression
plt.plot(x, expression)
plt.xlabel('x')
plt.ylabel('Expression Value')
plt.title('Plot of Expression')
plt.grid(True)
plt.show()
