import numpy as np
import matplotlib.pyplot as plt

def euler_method(f, x0, y0, h, x_end):
    x_values = [x0]
    y_values = [y0]
    x = x0
    y = y0
    while x < x_end:
        y = y + h * f(x, y)
        x = x + h
        x_values.append(x)
        y_values.append(y)
    return x_values, y_values

def euler_cauchy_method(f, x0, y0, h, x_end):
    x_values = [x0]
    y_values = [y0]
    x = x0
    y = y0
    while x < x_end:
        y_euler = y + h * f(x, y)
        y = y + (h / 2) * (f(x, y) + f(x + h, y_euler))
        x = x + h
        x_values.append(x)
        y_values.append(y)
    return x_values, y_values

# Завдання a)
f_a = lambda x, y: x + np.cos(y / np.exp(1))
x0_a, y0_a, x_end_a = 1.4, 2.5, 2.4
h = 0.1

# Метод Ейлера
x_values_a_euler, y_values_a_euler = euler_method(f_a, x0_a, y0_a, h, x_end_a)

# Метод Ейлера-Коші
x_values_a_cauchy, y_values_a_cauchy = euler_cauchy_method(f_a, x0_a, y0_a, h, x_end_a)

# Завдання б)
f_b = lambda x, y: x + np.sin(y * np.sqrt(7))
x0_b, y0_b, x_end_b = 0.5, 0.6, 1.5

# Метод Ейлера
x_values_b_euler, y_values_b_euler = euler_method(f_b, x0_b, y0_b, h, x_end_b)

# Метод Ейлера-Коші
x_values_b_cauchy, y_values_b_cauchy = euler_cauchy_method(f_b, x0_b, y0_b, h, x_end_b)

# Побудова графіків
plt.plot(x_values_a_euler, y_values_a_euler, label="Euler method (Task a)")
plt.plot(x_values_a_cauchy, y_values_a_cauchy, label="Euler-Cauchy method (Task a)")
plt.plot(x_values_b_euler, y_values_b_euler, label="Euler method (Task b)")
plt.plot(x_values_b_cauchy, y_values_b_cauchy, label="Euler-Cauchy method (Task b)")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Solutions for Euler and Euler-Cauchy methods")
plt.show()
