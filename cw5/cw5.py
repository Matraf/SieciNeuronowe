import copy
import math

C = 0.1
E = 0.000001
B = 1.0

u = [[0, 0, 1],
     [1, 0, 1],
     [0, 1, 1],
     [1, 1, 1]]
x = [[0.0, 0.0, 1.0],
     [0.0, 0.0, 1.0],
     [0.0, 0.0, 1.0],
     [0.0, 0.0, 1.0]]
w = [[0.0, 1.0, 2.0],
     [0.0, 1.0, 2.0]]
w_new = [[0.0, 0.0, 0.0],
         [0.0, 0.0, 0.0]]
s = [0.0, 1.0, 2.0]
s_new = [0.0, 0.0, 0.0]
y = [0.0, 0.0, 0.0, 0.0]
z = [0.0, 1.0, 1.0, 0.0]

de_s = [0, 0, 0]
de_w = [[0, 0, 0],
        [0, 0, 0]]


def f(_):
    try:
        return 1 / (1 + math.exp(- B * _))
    except OverflowError:
        return float('inf')


def df(param):
    t = f(param)
    return B * t * (1 - t)


def evaluate_de_s(ii):
    de_s[ii] = 0
    for p in [0, 1, 2, 3]:
        de_s[ii] = de_s[ii] + (y[p] - z[p]) * df(s[0] * x[p][0] + s[1] * x[p][1] + s[2] * x[p][2]) * x[p][ii]


def calculate_de_w(ii, jj):
    de_w[ii][jj] = 0
    for p in [0, 1, 2, 3]:
        de_w[ii][jj] = de_w[ii][jj] + (y[p] - z[p]) * df(s[0] * x[p][0] + s[1] * x[p][1] + s[2] * x[p][2]) * s[ii] * df(
            w[ii][0] * u[p][0] + w[ii][1] * u[p][1] + w[ii][2] * u[p][2]) * u[p][jj]


def evaluate_x():
    for p in [0, 1, 2, 3]:
        for i_ in [0, 1]:
            x[p][i_] = f(w[i_][0] * u[p][i_] + w[i_][1] * u[p][i_] + w[i_][2] * u[p][i_])


def evaluate_y():
    for p in [0, 1, 2, 3]:
        y[p] = f(s[0] * x[p][0] + s[1] * x[p][1] + s[2] * x[p][2])


def back_propagation():
    global s, w
    while True:
        max_ = -999
        evaluate_x()
        evaluate_y()
        for i in [0, 1, 2]:
            evaluate_de_s(i)
            s_new[i] = s[i] - C * de_s[i]
            if abs(s_new[i] - s[i]) > max_:
                max_ = abs(s_new[i] - s[i])
        for i in [0, 1]:
            for j in range(2):
                calculate_de_w(i, j)
                w_new[i][j] = w[i][j] - C * de_w[i][j]
                if abs(w_new[i][j] - w[i][j]) > max_:
                    max_ = abs(w_new[i][j] - w[i][j])
        if max_ < E:
            break
        s = copy.deepcopy(s_new)
        w = copy.deepcopy(w_new)

    print(w)
    print(s)
    for i in range(4):
        print(y[i])


if __name__ == '__main__':
    back_propagation()