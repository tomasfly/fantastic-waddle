import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 400)
y = 2*x**3 - 4*x**2 + 3*x - 5

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='P(x) = 2x^3 - 4x^2 + 3x - 5')
plt.title('Gráfico del Polinomio')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.legend()
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.show()
