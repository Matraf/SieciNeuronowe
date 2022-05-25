u = [
    {
        '[1, 1]': 0, '[1, 2]': 0, '[1, 3]': 0, '[1, 4]': 0, '[1, 5]': 0,
        '[2, 1]': 0, '[2, 2]': 1, '[2, 3]': 1, '[2, 4]': 1, '[2, 5]': 0,
        '[3, 1]': 0, '[3, 2]': 1, '[3, 3]': 0, '[3, 4]': 1, '[3, 5]': 0,
        '[4, 1]': 0, '[4, 2]': 1, '[4, 3]': 1, '[4, 4]': 1, '[4, 5]': 0,
        '[5, 1]': 0, '[5, 2]': 0, '[5, 3]': 0, '[5, 4]': 0, '[5, 5]': 0,
    },
    {
        '[1, 1]': 0, '[1, 2]': 0, '[1, 3]': 0, '[1, 4]': 0, '[1, 5]': 0,
        '[2, 1]': 0, '[2, 2]': 0, '[2, 3]': 0, '[2, 4]': 0, '[2, 5]': 0,
        '[3, 1]': 1, '[3, 2]': 1, '[3, 3]': 1, '[3, 4]': 0, '[3, 5]': 0,
        '[4, 1]': 1, '[4, 2]': 0, '[4, 3]': 1, '[4, 4]': 0, '[4, 5]': 0,
        '[5, 1]': 1, '[5, 2]': 1, '[5, 3]': 1, '[5, 4]': 0, '[5, 5]': 0,
    },
    {
        '[1, 1]': 0, '[1, 2]': 0, '[1, 3]': 0, '[1, 4]': 0, '[1, 5]': 0,
        '[2, 1]': 0, '[2, 2]': 1, '[2, 3]': 1, '[2, 4]': 0, '[2, 5]': 0,
        '[3, 1]': 0, '[3, 2]': 0, '[3, 3]': 1, '[3, 4]': 0, '[3, 5]': 0,
        '[4, 1]': 0, '[4, 2]': 0, '[4, 3]': 1, '[4, 4]': 0, '[4, 5]': 0,
        '[5, 1]': 0, '[5, 2]': 0, '[5, 3]': 1, '[5, 4]': 0, '[5, 5]': 0,
    },
    {
        '[1, 1]': 0, '[1, 2]': 0, '[1, 3]': 1, '[1, 4]': 1, '[1, 5]': 0,
        '[2, 1]': 0, '[2, 2]': 0, '[2, 3]': 0, '[2, 4]': 1, '[2, 5]': 0,
        '[3, 1]': 0, '[3, 2]': 0, '[3, 3]': 0, '[3, 4]': 1, '[3, 5]': 0,
        '[4, 1]': 0, '[4, 2]': 0, '[4, 3]': 0, '[4, 4]': 1, '[4, 5]': 0,
        '[5, 1]': 0, '[5, 2]': 0, '[5, 3]': 0, '[5, 4]': 0, '[5, 5]': 0,
    },
    {
        '[1, 1]': 0, '[1, 2]': 0, '[1, 3]': 0, '[1, 4]': 0, '[1, 5]': 0,
        '[2, 1]': 1, '[2, 2]': 1, '[2, 3]': 0, '[2, 4]': 0, '[2, 5]': 0,
        '[3, 1]': 0, '[3, 2]': 1, '[3, 3]': 0, '[3, 4]': 0, '[3, 5]': 0,
        '[4, 1]': 0, '[4, 2]': 1, '[4, 3]': 0, '[4, 4]': 0, '[4, 5]': 0,
        '[5, 1]': 0, '[5, 2]': 1, '[5, 3]': 0, '[5, 4]': 0, '[5, 5]': 0,
    }
]

w = [
    {
        '[-1, -1]': 1, '[-1, 0]': 1, '[-1, 1]': 1,
        '[0, -1]': 1, '[0, 0]': 0, '[0, 1]': 0,
        '[1, -1]': 1, '[1, 0]': 0, '[1, 1]': 0,
    },
    {
        '[-1, -1]': 0, '[-1, 0]': 0, '[-1, 1]': 1,
        '[0, -1]': 0, '[0, 0]': 0, '[0, 1]': 1,
        '[1, -1]': 1, '[1, 0]': 1, '[1, 1]': 1,
    },
    {
        '[-1, -1]': 1, '[-1, 0]': 1, '[-1, 1]': 0,
        '[0, -1]': 0, '[0, 0]': 1, '[0, 1]': 0,
        '[1, -1]': 0, '[1, 0]': 1, '[1, 1]': 0,
    },
    {
        '[-1, -1]': 0, '[-1, 0]': 1, '[-1, 1]': 0,
        '[0, -1]': 0, '[0, 0]': 1, '[0, 1]': 0,
        '[1, -1]': 0, '[1, 0]': 1, '[1, 1]': 0,
    }
]

threshold_2 = lambda a: 1 if a > 0.5 else 0
threshold = lambda x: 1 if x > 0 else 0

def printText(x):
    res = ""
    for i in x:
        if i == 0:
            res += "▒"
        else:
            res += "█"
    print(res)

def allConvolution():
    for x in range(5):
        for y in range(4):
            showX(convolution(u[x], w[y]), f'X = U{x + 1} * W{y + 1}')


def allPooling():
    for x in range(5):
        for y in range(4):
            showY(pooling(convolution(u[x], w[y])), x, y)


def showX(data, placeholder):
    print(placeholder)
    for x in range(1, 6):
        value = []
        for y in range(1, 6):
            value.append(readValue(x, y, data))
        printText(value)



def convolution(u, w):
    x = {}
    for i in range(1, 6):
        for j in range(1, 6):
            setValue(i, j, x, countUW(i, j, u, w))
    return x


def showY(data, x, y):
    print(str(x) + " " + str(y))
    for x in range(1, 3):
        value = []
        for y in range(1, 3):
            value.append(readValue(x, y, data))
        printText(value)


def pooling(x):
    y = {}
    for i in range(1, 3):
        for j in range(1, 3):
            setValue(i, j, y, threshold_2(countYValue(i, j, x)))
    return y


def readValue(x, y, data):
    tpl = f'[{x}, {y}]'
    value = data.get(tpl, 0)
    return value or 0


def setValue(i, j, data, value):
    tpl = f'[{i}, {j}]'
    data[tpl] = value


def countYValue(i, j, x):
    p = countP(i, j)
    sum = 0
    for k in range(0, len(p)):
        sum += readValue(p[k][0], p[k][1], x)
    return 1 / 16 * sum


def countP(i, j):
    p = []
    for k in range(0, 4):
        for l in range(0, 4):
            p.append([i + k, j + l])
    return p


def countUW(i, j, u, w):
    sum = 0
    for ii in range(-1, 2):
        for jj in range(-1, 2):
            sum += readValue(ii, jj, w) * readValue(i - ii, j - jj, u)
    return threshold(sum)


allConvolution()
allPooling()
