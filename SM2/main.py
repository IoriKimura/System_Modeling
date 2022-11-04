import matplotlib.pyplot as plt
import matplotlib
import numpy as sempai


def multiplic_rand_nums(a, b, x, m) -> float:
    return (a * x + b) % m


def random_num(A, B, x):
    return A + (B - A) * x


def math_wait(X):
    res = 0
    for i in range(len(X)):
        res += X[i]
    return res / len(X)


def dispersion(X, M):
    res = 0
    N = len(X)
    for i in range(len(X)):
        res += X[i] ** 2
    return (res / N - M ** 2) * N / (N - 1)


def random_period(Y: sempai.ndarray):
    count = 0
    for i in range(1, len(Y)):
        count += 1
        if f"{Y[i]:.3f}" == f"{Y[0]:.3f}":
            return count


def pirson(Y, np):
    pirson_cr = 0.0
    for j in range(len(Y)):
        n = Y[j] / np
        pirson_cr += (n - np) ** 2 / np
    return pirson_cr


def main():
    m = 2 ** 32
    b = 1
    a = 22695477
    A = 0
    B = 10
    Xrand_nums = sempai.empty(4, dtype=sempai.ndarray)
    Yrand_nums = sempai.empty(4, dtype=sempai.ndarray)

    for i in range(4):
        n = 10 ** (i + 2)
        Xi = sempai.empty(n, dtype=sempai.ndarray)
        x0 = 1
        for j in range(len(Xi)):
            Xi[j] = multiplic_rand_nums(a, b, x0, m)
            x0 = Xi[j]
            Xi[j] /= m
        Xrand_nums[i] = Xi

    for i in range(4):
        Yi = sempai.empty(len(Xrand_nums[i]), dtype=sempai.ndarray)
        for j in range(len(Yi)):
            Yi[j] = random_num(A, B, Xrand_nums[i][j])
        Yrand_nums[i] = Yi

    M_array = sempai.empty(4, dtype=sempai.ndarray)
    D_array = sempai.empty(4, dtype=sempai.ndarray)
    My_Periods = sempai.empty(4, dtype=sempai.ndarray)

    Rnd_Periods = sempai.empty(4, dtype=sempai.ndarray)

    for i in range(4):
        M_array[i] = math_wait(Yrand_nums[i])
        print(f"Мат.ожидание {i + 1}:{M_array[i]}")
        D_array[i] = dispersion(Yrand_nums[i], M_array[i])
        print(f"Дисперсия {i + 1}:{D_array[i]}")
        My_Periods[i] = random_period(Yrand_nums[i])

        Rnd_Periods[i] = random_period(sempai.random.default_rng(12345).random(size=10 ** (i + 2)))

    for i in range(len(My_Periods)):
        print(f"Период собственного алгоритма:{My_Periods[i]}")
        print(f"Период встроенного генератора:{Rnd_Periods[i]}")

    Pirsons = sempai.empty(4, dtype=sempai.ndarray)

    for i in range(len(Yrand_nums)):
        plt.title(f"Гистограмма при {i}")
        plt.hist(Yrand_nums[i], bins=10, density=True)
        if My_Periods[i] is not None:
            Pirsons[i] = pirson(Yrand_nums[i], My_Periods[i])
        plt.show()

    for p in Pirsons:
        print(f"Значение пирсона:{p}")


if __name__ == "__main__":
    main()

