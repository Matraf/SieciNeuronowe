import random

c = 0.01
E = 0.0000001


def derivative_x(x, y, z):
    return 4 * x - 2 * y - 2


def derivative_y(x, y, z):
    return 4 * y - 2 * x - 2 * z


def derivative_z(x, y, z):
    return 2 * z - 2 * y


def derivative_x2(x, y):
    return 12 * x ** 3 + 12 * x ** 2 - 24 * x


def derivative_y2(x, y):
    return 24 * y - 24


x_old, y_old, z_old = random.random(), random.random(), random.random()

max_ = 0
x_new, y_new, z_new = 0, 0, 0

while True:
    x_new = x_old - c * derivative_x(x_old, y_old, z_old)
    y_new = y_old - c * derivative_y(x_old, y_old, z_old)
    z_new = z_old - c * derivative_z(x_old, y_old, z_old)

    max_ = 0
    if abs(x_new - x_old) > max_:
        max_ = abs(x_new - x_old)
    if abs(y_new - y_old) > max_:
        max_ = abs(y_new - y_old)
    if abs(z_new - z_old) > max_:
        max_ = abs(z_new - z_old)
    if max_ < E:
        break

    x_old, y_old, z_old = x_new, y_new, z_new

print(x_new, y_new, z_new,
      2 * x_new ** 2 + 2 * y_new ** 2 + z_new ** 2 - 2 * x_new * y_new - 2 * y_new * z_new - 2 * x_new + 3)


x_old, y_old = random.random(), random.random()

max_ = 0
x_new, y_new = 0, 0

while True:
    x_new = x_old - c * derivative_x2(x_old, y_old)
    y_new = y_old - c * derivative_y2(x_old, y_old)

    max_ = 0
    if abs(x_new - x_old) > max_:
        max_ = abs(x_new - x_old)
    if abs(y_new - y_old) > max_:
        max_ = abs(y_new - y_old)
    if max_ < E:
        break

    x_old, y_old = x_new, y_new

print(x_new, y_new, 3 * x_new ** 4 + 4 * x_new ** 3 - 12 * x_new ** 2 + 12 * y_new ** 2 - 24 * y_new)
