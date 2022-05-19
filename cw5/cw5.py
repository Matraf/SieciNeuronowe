import math

c = 1.0
epsilon = 0.001
beta = 1.25

u = [[0.0, 0.0, 1.0],
     [0.0, 1.0, 1.0],
     [1.0, 0.0, 1.0],
     [1.0, 1.0, 1.0]]
Z = [0.0, 1.0, 1.0, 0.0]

W = [[0.0, 1.0, 2.0],
     [0.0, 1.0, 2.0]]

X = [3.0, 3.0, 1.0]
s = [0, 1, 2]

def f(x):
    return 1/(1 + math.pow(math.e, -beta * x))

def vp():
    return s[0] * X[0] + s[1] * X[1] + s[2] * X[2]

def Df(x):
    return beta * f(x) * (1 - f(x))

def newS(_s):
    s_new = [0.0, 0.0, 0.0]
    for i in range (0, len(s)):
        s_new[i] = s[i] - c * Es(i)
    
    return s_new

def newW(w):
    w_new = [[0.0, 0.0, 0.0],
             [0.0, 0.0, 0.0]]
    
    for i in range(0, 2):
        for j in range(0, 3):
            w_new[i][j] = w[i][j] - c * Ew(i, j)
    return w_new

def newX(index):
    for i in range(0, len(X)-1):
        X[i] = f(W[i][0] * u[index][0] + W[i][1] * u[index][1] + W[i][2])

def Fp(index):
    newX(index)
    return vp()

def _max(_s, sp, w, wp):
    maximum = 0
    for k in range(0, len(_s)):
        sa = abs(sp[k] - _s[k])
        for l in range(0, len(w)):
            wa = abs(wp[l][k] - w[l][k])
            if wa >= maximum:
                maximum = wa
        if sa >= maximum:
            maximum = sa
    return maximum

def Es(index):
    _sum = 0
    for i in range(0, len(Z)):
        x = Fp(i)
        y = f(x)
        _sum += ((y - Z[i]) * Df(vp()) * X[index])
    return _sum

def Ew(wi, wj):
    _sum = 0
    for i in range(0, len(Z)):
        newX(i)
        x = Fp(i)
        y = f(x)
        temp = W[wi][0] * u[i][0] + W[wi][1] * u[i][1] + W[wi][2]
        _sum += (y - Z[i]) * Df(vp()) * s[wi] * Df(temp) * u[i][wj]
    return _sum

def back_propagation():
    global s, W
    _maximum = 0
    while True:
        s_new = newS(s)
        w_new = newW(W)
        _maximum = _max(s, s_new, W, w_new)
        s = s_new.copy()
        W = w_new.copy()
        print(_maximum)
        if _maximum <= epsilon:
            break
    print(X)
    print(W)
    print(s)
    for i in range(0, 4):
        print("y[" + str(i) + "] = " + str(f(Fp(i))))


if __name__ == '__main__':
    back_propagation()
