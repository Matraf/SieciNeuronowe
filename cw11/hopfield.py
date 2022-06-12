from random import random

n = 25

x = [round(random()) for _ in range(n)]
u = [0] * n

z = (0, 0, 0, 0, 0,
     0, 1, 1, 0, 0,
     0, 0, 1, 0, 0,
     0, 0, 1, 0, 0,
     0, 0, 1, 0, 0)
z_prim = (0, 1, 1, 1, 0,
          0, 1, 0, 1, 0,
          0, 1, 0, 1, 0,
          0, 1, 0, 1, 0,
          0, 1, 1, 1, 0)

c = [[0 for _ in range(25)] for _ in range(25)]
d = [[0 for _ in range(25)] for _ in range(25)]
w = [[0 for _ in range(25)] for _ in range(25)]
w_prim = [[0 for _ in range(25)] for _ in range(25)]
theta = [0] * 25
theta_prim = [0] * 25


def calc_cd():
    for i in range(25):
        for j in range(25):
            c[i][j] = (z[i] - 0.5) * (z[j] - 0.5) if i != j else 0
            d[i][j] = (z_prim[i] - 0.5) * (z_prim[j] - 0.5) if i != j else 0


def calc_w():
    for i in range(25):
        for j in range(25):
            w[i][i] = 2 * c[i][j]
            w_prim[i][j] = 2 * (c[i][j] + d[i][j])


def calc_theta():
    for i in range(25):
        theta[i] = sum(c[i])
        theta_prim[i] = sum(c[i] + d[i])


def calc_u(task):
    if task == 1:
        for i in range(n):
            temp_sum = 0
            for j in range(n):
                temp_sum += w[i][j] * x[j]
            u[i] = temp_sum - theta[i]
    else:
        for i in range(n):
            temp_sum = 0
            for j in range(n):
                temp_sum += w_prim[i][j] * x[j]
            u[i] = temp_sum - theta_prim[i]


def calc_x(step, task):
    if step != 0:
        calc_u(task)
        for i in range(n):
            if u[i] < 0:
                x[i] = 0
            elif u[i] > 0:
                x[i] = 1


def calc_params():
    calc_cd()
    calc_w()
    calc_theta()


def reset_x():
    x = [round(random()) for _ in range(n)]
    u = [0] * n


def hopfield_network():
    t = 0
    calc_params()
    print('===== HOPFIELD NETWORK =====')
    for task in (1, 2):
        reset_x()
        print(f'----- TASK {task} -----')
        for i in range(3):
            calc_x(t, task)
            print(f'Step {t}')
            for j in range(n):
                if x[j] == 1:
                    print(u'\u2b1b', end=' ')
                else:
                    print(u'\u2b1c', end=' ')
                if (j + 1) % 5 == 0:
                    print()
            print()
            t += 1
        t = 0


if __name__ == '__main__':
    hopfield_network()
