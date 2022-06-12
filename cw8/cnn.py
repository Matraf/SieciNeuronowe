u = [
{
        '(1, 1)': 0, '(1, 2)': 0, '(1, 3)': 0, '(1, 4)': 0, '(1, 5)': 0,
        '(2, 1)': 0, '(2, 2)': 1, '(2, 3)': 1, '(2, 4)': 1, '(2, 5)': 0,
        '(3, 1)': 0, '(3, 2)': 1, '(3, 3)': 0, '(3, 4)': 1, '(3, 5)': 0,
        '(4, 1)': 0, '(4, 2)': 1, '(4, 3)': 1, '(4, 4)': 1, '(4, 5)': 0,
        '(5, 1)': 0, '(5, 2)': 0, '(5, 3)': 0, '(5, 4)': 0, '(5, 5)': 0,
    },
    {
        '(1, 1)': 0, '(1, 2)': 0, '(1, 3)': 0, '(1, 4)': 0, '(1, 5)': 0,
        '(2, 1)': 0, '(2, 2)': 0, '(2, 3)': 0, '(2, 4)': 0, '(2, 5)': 0,
        '(3, 1)': 1, '(3, 2)': 1, '(3, 3)': 1, '(3, 4)': 0, '(3, 5)': 0,
        '(4, 1)': 1, '(4, 2)': 0, '(4, 3)': 1, '(4, 4)': 0, '(4, 5)': 0,
        '(5, 1)': 1, '(5, 2)': 1, '(5, 3)': 1, '(5, 4)': 0, '(5, 5)': 0,
    },
    {
        '(1, 1)': 0, '(1, 2)': 0, '(1, 3)': 0, '(1, 4)': 0, '(1, 5)': 0,
        '(2, 1)': 0, '(2, 2)': 1, '(2, 3)': 1, '(2, 4)': 0, '(2, 5)': 0,
        '(3, 1)': 0, '(3, 2)': 0, '(3, 3)': 1, '(3, 4)': 0, '(3, 5)': 0,
        '(4, 1)': 0, '(4, 2)': 0, '(4, 3)': 1, '(4, 4)': 0, '(4, 5)': 0,
        '(5, 1)': 0, '(5, 2)': 0, '(5, 3)': 1, '(5, 4)': 0, '(5, 5)': 0,
    },
    {
        '(1, 1)': 0, '(1, 2)': 0, '(1, 3)': 1, '(1, 4)': 1, '(1, 5)': 0,
        '(2, 1)': 0, '(2, 2)': 0, '(2, 3)': 0, '(2, 4)': 1, '(2, 5)': 0,
        '(3, 1)': 0, '(3, 2)': 0, '(3, 3)': 0, '(3, 4)': 1, '(3, 5)': 0,
        '(4, 1)': 0, '(4, 2)': 0, '(4, 3)': 0, '(4, 4)': 1, '(4, 5)': 0,
        '(5, 1)': 0, '(5, 2)': 0, '(5, 3)': 0, '(5, 4)': 0, '(5, 5)': 0,
    },
    {
        '(1, 1)': 0, '(1, 2)': 0, '(1, 3)': 0, '(1, 4)': 0, '(1, 5)': 0,
        '(2, 1)': 1, '(2, 2)': 1, '(2, 3)': 0, '(2, 4)': 0, '(2, 5)': 0,
        '(3, 1)': 0, '(3, 2)': 1, '(3, 3)': 0, '(3, 4)': 0, '(3, 5)': 0,
        '(4, 1)': 0, '(4, 2)': 1, '(4, 3)': 0, '(4, 4)': 0, '(4, 5)': 0,
        '(5, 1)': 0, '(5, 2)': 1, '(5, 3)': 0, '(5, 4)': 0, '(5, 5)': 0,
    }
]

w = [
    {
        '(-1, -1)': 1, '(-1, 0)': 1, '(-1, 1)': 1,
        '(0, -1)': 1, '(0, 0)': 0, '(0, 1)': 0,
        '(1, -1)': 1, '(1, 0)': 0, '(1, 1)': 0,
    },
    {
        '(-1, -1)': 0, '(-1, 0)': 0, '(-1, 1)': 1,
        '(0, -1)': 0, '(0, 0)': 0, '(0, 1)': 1,
        '(1, -1)': 1, '(1, 0)': 1, '(1, 1)': 1,
    },
    {
        '(-1, -1)': 1, '(-1, 0)': 1, '(-1, 1)': 0,
        '(0, -1)': 0, '(0, 0)': 1, '(0, 1)': 0,
        '(1, -1)': 0, '(1, 0)': 1, '(1, 1)': 0,
    },
    {
        '(-1, -1)': 0, '(-1, 0)': 1, '(-1, 1)': 0,
        '(0, -1)': 0, '(0, 0)': 1, '(0, 1)': 0,
        '(1, -1)': 0, '(1, 0)': 1, '(1, 1)': 0,
    }
]


def threshold(x):
    return 1 if x > 0 else 0


def threshold_2(x):
    return 1 if x > 0.5 else 0


def read_value(x, y, data):
    tpl = f'({x}, {y})'
    value = data.get(tpl, 0)
    return value or 0


def set_value(i, j, data, value):
    tpl = f'({i}, {j})'
    data[tpl] = value


def count_uw(i, j, u, w):
    sum = 0
    for ii in range(-1, 2):
        for jj in range(-1, 2):
            sum += read_value(ii, jj, w) * read_value(i - ii, j - jj, u)
    return threshold(sum)


def convolution(u, w):
    x = {}
    for i in range(1, 6):
        for j in range(1, 6):
            set_value(i, j, x, count_uw(i, j, u, w))
    return x


def count_y_value(i, j, x):
    p = count_p(i, j)
    sum = 0
    for k in range(0, len(p)):
        sum += read_value(p[k][0], p[k][1], x)
    return 1 / 16 * sum


def count_p(i, j):
    p = []
    for k in range(0, 4):
        for l in range(0, 4):
            p.append([i + k, j + l])
    return p


def printText(x):
    res = ""
    for i in x:
        if i == 0:
            res += "▒"
        else:
            res += "█"
    print(res)


def showX(data, placeholder):
    print(placeholder)
    for x in range(1, 6):
        value = []
        for y in range(1, 6):
            value.append(read_value(x, y, data))
        printText(value)


def showY(data, x, y):
    print(str(x) + " " + str(y))
    for x in range(1, 3):
        value = []
        for y in range(1, 3):
            value.append(read_value(x, y, data))
        printText(value)


def allConvolution():
    for x in range(5):
        for y in range(4):
            showX(convolution(u[x], w[y]), f'X = U{x + 1} * W{y + 1}')


def pooling(x):
    y = {}
    for i in range(1, 3):
        for j in range(1, 3):
            set_value(i, j, y, threshold_2(count_y_value(i, j, x)))
    return y


def allPooling():
    for x in range(5):
        for y in range(4):
            showY(pooling(convolution(u[x], w[y])), x, y)


allConvolution()
allPooling()
