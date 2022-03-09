u1 = [0, 0, 0, 0, 0,
      0, 1, 1, 1, 0,
      0, 1, 0, 1, 0,
      0, 1, 1, 1, 0,
      0, 0, 0, 0, 0, 1]

u2 = [0, 0, 0, 0, 0,
      0, 0, 0, 0, 0,
      1, 1, 1, 0, 0,
      1, 0, 1, 0, 0,
      1, 1, 1, 0, 0, 1]

u3 = [0, 0, 0, 0, 0,
      0, 1, 1, 0, 0,
      0, 0, 1, 0, 0,
      0, 0, 1, 0, 0,
      0, 0, 1, 0, 0, 1]

u4 = [0, 0, 1, 1, 0,
      0, 0, 0, 1, 0,
      0, 0, 0, 1, 0,
      0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 1]

u5 = [0, 0, 0, 0, 0,
      1, 1, 0, 0, 0,
      0, 1, 0, 0, 0,
      0, 1, 0, 0, 0,
      0, 1, 0, 0, 0, 1]

u = [u1, u2, u3, u4, u5]


def perceptron_learning(c):
    w = [1] * 26
    t = 0
    counter = 0
    while counter != 5:
        z = +((t % 5) > 2)
        y = f(w, u, t)
        for i in range(len(u[t % 5])):
            w[i] = w[i] + c * (z - y) * u[(t % 5)][i]

        if z == y:
            counter = counter + 1
        else:
            counter = 0

        t = t + 1

    return t + 1, w


def f(w, u, t):
    return +(sum(w[j] * u[(t % 5)][j] for j in range(len(u[(t % 5)]))) >= 0)


if __name__ == '__main__':
    print(perceptron_learning(0.1))
