import numpy as np
import matplotlib.pyplot as plt

# Задана функція f(x, y)
def f(x, y):
    return np.sin(x) - np.cos(y)

# Метод Ейлера
def euler_method(f, x0, y0, h, n):
    x_values = [x0]
    y_values = [y0]
    x = x0
    y = y0
    for i in range(n):
        y = y + h * f(x, y)
        x = x + h
        x_values.append(x)
        y_values.append(y)
    return x_values, y_values

# Параметри задачі
x0 = 0
y0 = 1
h = 0.2  # крок
n = 5    # кількість кроків

# Обчислення методом Ейлера
x_values, y_values = euler_method(f, x0, y0, h, n)

# Виведення результатів у вигляді таблиці
print("i\txi\tyi")
for i in range(len(x_values)):
    print(f"{i}\t{x_values[i]:.1f}\t{y_values[i]:.4f}")

# Побудова графіку
plt.plot(x_values, y_values, 'o-', label="Точки")
plt.plot(x_values, np.sin(x_values) - np.cos(y_values), label="sin(x) - cos(y)")
plt.title("Метод Ейлера")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
