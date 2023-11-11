import numpy as np
import matplotlib.pyplot as plt

# Y(x)


def Y(x):
    return x * np.sin(5 * x)


# діапазон значень x
x_values = np.linspace(-2, 5, 400)

# значення Y(x)
y_values = Y(x_values)

# Побудова графіка
plt.plot(x_values, y_values, linestyle='-', color='blue',
         linewidth=2, label='Y(x) = x * sin(5 * x)')

# Позначення осей та назва графіка
plt.xlabel('x')
plt.ylabel('Y(x)')
plt.title('Графік функції Y(x) = x * sin(5 * x)')

# Легенда
plt.legend()

# Відображення графіка
plt.grid(True)
plt.show()
