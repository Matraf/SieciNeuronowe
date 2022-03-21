import random

c = 0.01
eps = 0.0000001


def derivative_x(x, y):
    return 4 * x - 2 * y - 2


def derivative_y(x, y, z):
    return 4 * y - 2 * x - 2 * z


def derivative_z(y, z):
    return 2 * z - 2 * y


def derivative_x2(x):
    return 12 * x ** 3 + 12 * x ** 2 - 24 * x


def derivative_y2(y):
    return 24 * y - 24


def first_function(x_old, y_old, z_old):
    x_new, y_new, z_new = 0, 0, 0
    max = 0
    while max < eps:
        x_new = x_old - c * derivative_x(x_old, y_old)
        y_new = y_old - c * derivative_y(x_old, y_old, z_old)
        z_new = z_old - c * derivative_z(y_old, z_old)

        max = 0
        if abs(x_new - x_old) > max:
            max = abs(x_new - x_old)
        if abs(y_new - y_old) > max:
            max = abs(y_new - y_old)
        if abs(z_new - z_old) > max:
            max = abs(z_new - z_old)

        x_old, y_old, z_old = x_new, y_new, z_new
    print(x_new, y_new, z_new,
          2 * x_new ** 2 + 2 * y_new ** 2 + z_new ** 2 - 2 * x_new * y_new - 2 * y_new * z_new - 2 * x_new + 3)


def second_function(x_old, y_old):
    max = 0
    x_new, y_new = 0, 0
    while max < eps:
        x_new = x_old - c * derivative_x2(x_old)
        y_new = y_old - c * derivative_y2(y_old)

        max = 0
        if abs(x_new - x_old) > max:
            max = abs(x_new - x_old)
        if abs(y_new - y_old) > max:
            max = abs(y_new - y_old)

        x_old, y_old = x_new, y_new

    print(x_new, y_new,
          3 * x_new ** 4 + 4 * x_new ** 3 - 12 * x_new ** 2 + 12 * y_new ** 2 - 24 * y_new)


if __name__ == '__main__':
    x, y, z = random.random(), random.random(), random.random()
    first_function(x, y, z)
    second_function(x, y)
