from math import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


def normal_distribution(x):
    return (1 / (2 * (2 * pi) ** 0.5)) * exp(-((x - 10) ** 2) / (2 * 2 ** 2))


# def normal_distribution(x, m, sigma) -> float:
#  return (1 / (sigma * (2 * pi)**0.5)) * exp(-((x - m)**2) / (2 * sigma**2))


def distribution_function_method(x):
    return quad(normal_distribution, -inf, x)[0]


def model(x_tab, y_tab, p):
    for i in range(1, len(x_tab)):
        if y_tab[i - 1] <= p <= y_tab[i]:
            a = ((p - y_tab[i]) / (y_tab[i - 1] - y_tab[i])) * x_tab[i - 1]
            b = ((p - y_tab[i - 1]) / (y_tab[i] - y_tab[i - 1])) * x_tab[i]
            y = a + b
            return y


def distr(array, a, b, count):
    dy = (b - a) / count
    freq = [0] * count
    for j in range(len(array)):
        yc = array[j]
        fn = floor(yc / dy)
        freq[fn] += 1
    for i in range(count):
        freq[i] = freq[i] / (len(array) * dy)
    return freq


# Task1
def first_task():
    x = np.arange(0, 20, 0.01)

    normal_distribution_10_2 = list()
    for i in range(len(x)):
        normal_distribution_10_2.append(normal_distribution(x[i], 10, 2))
    plt.plot(x, normal_distribution_10_2, label='normal_distribution_10_2')

    normal_distribution_10_1 = list()
    for i in range(len(x)):
        normal_distribution_10_1.append(normal_distribution(x[i], 10, 1))
    plt.plot(x, normal_distribution_10_1, label='normal_distribution_10_1')

    normal_distribution_10_05 = list()
    for i in range(len(x)):
        normal_distribution_10_05.append(normal_distribution(x[i], 10, 0.5))
    plt.plot(x, normal_distribution_10_05, label='normal_distribution_10_05')

    normal_distribution_12_1 = list()
    for i in range(len(x)):
        normal_distribution_12_1.append(normal_distribution(x[i], 12, 1))
    plt.plot(x, normal_distribution_12_1, label='normal_distribution_12_1')
    plt.legend()
    plt.show()


# Task2
def second_task():
    x = np.arange(0, 20, 0.01)
    distribution_function = list()
    for i in range(len(x)):
        distribution_function.append(quad(normal_distribution, -inf, x[i])[0])

    plt.plot(x, distribution_function, label='distribution_function')

    plt.legend()
    plt.show()


# Task3
def third_task():
    x_tab = np.arange(0, 20, 0.001)
    y_tab = list()
    for i in range(len(x_tab)):
        y_tab.append(distribution_function_method(x_tab[i]))
    p = np.arange(0, 1, 0.00005)
    res_y = list()
    for i in range(len(p)):
        res_y.append(model(x_tab, y_tab, p[i]))
    plt.plot(p, res_y)
    plt.show()


# Task4-5
def fourth_and_fifth_tasks():
    figure, axis = plt.subplots(2, 2)
    n = 10 ** 3

    resx = np.arange(0, 20, 0.2)
    x_tab = np.arange(0, 20, 20 / n)
    y_tab = list()
    normal_distribution_array = list()
    for i in range(len(resx)):
        normal_distribution_array.append(normal_distribution(resx[i]))
    for i in range(len(x_tab)):
        y_tab.append(distribution_function_method(x_tab[i]))
    p_array = np.random.uniform(0, 1, n)
    res_y = list()
    for i in range(len(p_array)):
        res_y.append(model(x_tab, y_tab, p_array[i]))
    resy_e3 = distr(res_y, 0, 20, 100)
    axis[0, 0].bar(resx, resy_e3, label='resy_e3')
    axis[0, 0].plot(resx, normal_distribution_array, label='f(x_tab)', color='yellow')
    e0 = 0
    for i in range(100):
        e0 += (normal_distribution_array[i] - resy_e3[i]) ** 2
    e0 /= 100
    axis[0, 0].set_title(f'E0 = {e0} \n n = {n}')
    axis[0, 0].legend()

    n = 10 ** 4
    x_tab = np.arange(0, 20, 20 / n)
    y_tab = list()
    normal_distribution_array = list()
    for i in range(len(resx)):
        normal_distribution_array.append(normal_distribution(resx[i]))
    for i in range(len(x_tab)):
        y_tab.append(distribution_function_method(x_tab[i]))
    p_array = np.random.uniform(0, 1, n)
    res_y = list()
    for i in range(len(p_array)):
        res_y.append(model(x_tab, y_tab, p_array[i]))
    resy_e3 = distr(res_y, 0, 20, 100)
    axis[0, 1].bar(resx, resy_e3, label='resy_e3')
    axis[0, 1].plot(resx, normal_distribution_array, label='f(x_tab)', color='yellow')
    e1 = 0
    for i in range(100):
        e1 += (normal_distribution_array[i] - resy_e3[i]) ** 2
    e1 /= 100
    axis[0, 1].set_title(f'E1 = {e1} \n n = {n}')
    axis[0, 1].legend()

    n = 10 ** 5
    x_tab = np.arange(0, 20, 20 / n)
    y_tab = list()
    normal_distribution_array = list()
    for i in range(len(resx)):
        normal_distribution_array.append(normal_distribution(resx[i]))
    for i in range(len(x_tab)):
        y_tab.append(distribution_function_method(x_tab[i]))
    p_array = np.random.uniform(0, 1, n)
    res_y = list()
    for i in range(len(p_array)):
        res_y.append(model(x_tab, y_tab, p_array[i]))
    resy_e3 = distr(res_y, 0, 20, 100)
    axis[1, 0].bar(resx, resy_e3, label='resy_e3')
    axis[1, 0].plot(resx, normal_distribution_array, label='f(x_tab)', color='yellow')
    e2 = 0
    for i in range(100):
        e2 += (normal_distribution_array[i] - resy_e3[i]) ** 2
    e2 /= 100
    axis[1, 0].set_title(f'E2 = {e2} \n n = {n}')
    axis[1, 0].legend()

    e = [e0, e1, e2]
    n_array = [10 ** 3, 10 ** 4, 10 ** 5]
    axis[1, 1].plot(n_array, e)
    axis[1, 1].set_title('dependence of E on the number of elements')
    axis[1, 1].legend()

    plt.show()


def main():
    #first_task()
    second_task()
    third_task()
    fourth_and_fifth_tasks()


if __name__ == '__main__':
    main()
