import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 400)
y = np.linspace(0, 10, 400)

x_min, x_max = min(x), max(x)
y_min, y_max = min(y), max(y)
step_size = 1.0

x, y = np.meshgrid(x, y)

"""
You can change this formula
Default formula: y = x **2
"""
formula = (- y + x ** 2)

plt.contour(x, y, formula, [0], colors='k')


plt.grid(True)
plt.xticks(np.arange(x_min, x_max+1, step_size))
plt.yticks(np.arange(y_min, y_max+1, step_size))
plt.show()
