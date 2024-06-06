import numpy as np
import matplotlib.pyplot as plt


def coord(x, y, e):
    xn, yn = x, y
    path = [(xn, yn)]
    while True:
        xn = gold(lambda n: func(n, yn), a, b, e)
        path.append((xn, yn))

        yn = gold(lambda n: func(xn, n), c, d, e)
        path.append((xn, yn))

        if ((path[-1][0] - path[-2][0]) ** 2 + (path[-1][1] - path[-2][1]) ** 2) ** 0.5 < e:
            break

    return xn, yn, path

def gold(lam, a, b, e):
    k = (1 + 5 ** 0.5) / 2

    l = b - (b - a) / k
    r = a + (b - a) / k

    while abs(b - a) > e:
        if lam(l) < lam(r):
            b = r
        else:
            a = l

        l = b - (b - a) / k
        r = a + (b - a) / k

    return (a + b) / 2



def grad(x, y, e):
    xn, yn = x, y
    path = [(xn, yn)]
    while True:
        gradX = (func(xn + e, yn) - func(xn, yn)) / e
        gradY = (func(xn, yn + e) - func(xn, yn)) / e

        alphaX = gold(lambda alpha: func(xn - alpha * gradX, yn), a, b, e)
        alphaY = gold(lambda alpha: func(xn, yn - alpha * gradY), c, d, e)

        xn = xn - alphaX * gradX
        yn = yn - alphaY * gradY

        path.append((xn, yn))

        if (gradX ** 2 + gradY ** 2) ** (0.5) < e:
            break

    return xn, yn, path
    
def func(x, y):
    return (x - 5) ** 2 + (y - 5) ** 2  

def main():
    try:
        e = float(input("ε = "))
        x = float(input("x = "))
        y = float(input("y = "))
        method = input("Методы:\n1) покоординатный спуск \n2) наискорейший градиентный спуск\nМетод = ")

        if method == '1':
            minX, minY, path = coord(x, y, e)
        elif method == '2':
            minX, minY, path = grad(x, y, e)
        else:
            raise
    except:
        exit()

    res = func(minX, minY)

    path_x = [point[0] for point in path]
    path_y = [point[1] for point in path]
    plt.plot(path_x, path_y, 'r-o')

    gridX, gridY = np.meshgrid(np.linspace(a, b, 100), np.linspace(c, d, 100))
    z = func(gridX, gridY)
    contours = plt.contour(gridX, gridY, z, 20)

    plt.suptitle(f"x = {x}, y = {y}\nМинимум функции = {res}")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.clabel(contours, inline=True, fontsize=5)
    plt.show()

a, b, c, d = 0, 10, 0, 10
main()