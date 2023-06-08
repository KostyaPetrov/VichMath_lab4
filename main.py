import math
import os
import matplotlib.pyplot as plt


def main():
    j = 0
    while j == 0:
        print('Введите цифру 1, если хотите ввести данные с консоли. Введите 2, если хотите прочитать данные из файла')
        try:
            num_read = int(input())
            if num_read != 1 and num_read != 2:
                print("Вы должны ввести число 1 или 2 в зависимости от способа чтения данных")
            else:
                j = 1
        except ValueError:
            print("Вы должны ввести число 1 или 2")

    list_data = readData(num_read)

    j = 0
    while j == 0:
        print('Введите цифру 1, если хотите вывести данные в консоль. Введите 2, если хотите записать данные в файл')
        try:
            num_print = int(input())
            if num_print != 1 and num_print != 2:
                print("Вы должны ввести число 1 или 2 в зависимости от способа вывода данных")
            else:
                j = 1
        except ValueError:
            print("Вы должны ввести число 1 или 2")

    filename = ""
    if (num_print == 2):
        print("Введите путь к файлу")
        filename = str(input())

    name1, sko1, func1 = linearApproximation(list_data, num_print, filename)
    name2, sko2, func2 = secondPolynomialApproximation(list_data, num_print, filename)
    name3, sko3, func3 = thirdPolynomialApproximation(list_data, num_print, filename)
    name4, sko4, func4 = power_approximation(list_data, num_print, filename)
    name5, sko5, func5 = exponential_approximation(list_data, num_print, filename)
    name6, sko6, func6 = logarithmic_approximation(list_data, num_print, filename)

    list_sko = [sko1, sko2, sko3, sko4, sko5, sko6]
    list_name = [name1, name2, name3, name4, name5, name6]
    list_func=[func1,func2,func3,func4,func5,func6]

    name, sko = best_approximation(list_sko, list_name)

    print("Лучшая аппроксимация", name, "имеет ско", sko)


    drow_data(list_data, list_func,list_name)





def drow_data(data, func, names):
    list_x=[]
    list_y=[]
    colors=["red","blue","brown", "yellow", "green","orange"]
    for i in range(0, len(data), 2):
        list_x.append(data[i])
        list_y.append(data[i+1]+1)

    plt.scatter(list_x, list_y, label='Исходные данные')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid()
    plt.title('Аппроксимация функции')

    for i in range(0,len(names)):
        plt.plot(func[i], label=names[i], color=colors[i])

    plt.legend()
    plt.show()


def linearApproximation(list_points, num_print, path):
    num_point = len(list_points)
    list_x = []
    list_y = []
    sum_xy = 0
    for i in range(0, num_point, 2):
        sum_xy += list_points[i] * list_points[i + 1]
        # aga=i//2
        list_x.append(list_points[i])
        list_y.append(list_points[i + 1])

    sum_x = 0
    sum_xx = 0
    for i in range(0, num_point, 2):
        sum_x += list_points[i]
        sum_xx += list_points[i] ** 2

    sum_y = 0
    for i in range(0, num_point, 2):
        sum_y += list_points[i + 1]

    a = (num_point / 2 * sum_xy - sum_x * sum_y) / (num_point / 2 * sum_xx - sum_x ** 2)

    b = (sum_y - a * sum_x) / (num_point / 2)

    list_f = []
    for i in range(0, len(list_x)):
        list_f.append(a * list_x[i] + b)

    list_e = []
    s = 0
    for i in range(0, len(list_y)):
        list_e.append(list_f[i] - list_y[i])
        s += list_e[i] ** 2

    sko = math.sqrt(s / len(list_x))

    x_med = sum(list_x) / len(list_x)
    y_med = sum(list_y) / len(list_y)

    numerator_correlation = 0
    denominator_correlation = 0
    sum1 = 0
    sum2 = 0
    for i in range(0, len(list_x)):
        numerator_correlation += (list_x[i] - x_med) * (list_y[i] - y_med)
        sum1 += (list_x[i] - x_med) ** 2
        sum2 += (list_y[i] - y_med) ** 2

    denominator_correlation = math.sqrt(sum1 * sum2)

    final_correlation = numerator_correlation / denominator_correlation

    if num_print == 1:
        print("Линейная аппроксимация")
        # print("\n")

        print("x", end='        ')
        for i in range(0, len(list_x)):
            print(round(list_x[i], 3), end='        ')
        print()

        print("y", end='        ')
        for i in range(0, len(list_y)):
            print(round(list_y[i], 3), end='        ')
        print()

        print("f(x)", end='     ')
        for i in range(0, len(list_f)):
            print(round(list_f[i], 3), end='      ')
        print()

        print("e", end='        ')
        for i in range(0, len(list_e)):
            print(round(list_e[i], 3), end='      ')
        print()

        print("Функция: y =", a, "x +", b)

        print("Отклонение: S =", s)

        print("Среднеквадратическое отклонение: sko =", sko)

        print("Коффициент корреляции Пирсона: r =", final_correlation)

        print("\n\n")


    else:

        with open(path, 'w') as file:
            print("Линейная аппроксимация", file=file)
            print("\n", file=file)

            print("x", end='        ', file=file)
            for i in range(0, len(list_x)):
                print(round(list_x[i], 3), end='        ', file=file)
            print("\n", file=file)

            print("y", end='        ', file=file)
            for i in range(0, len(list_y)):
                print(round(list_y[i], 3), end='        ', file=file)
            print("\n", file=file)

            print("f(x)", end='     ', file=file)
            for i in range(0, len(list_f)):
                print(round(list_f[i], 3), end='      ', file=file)
            print("\n", file=file)

            print("e", end='        ', file=file)
            for i in range(0, len(list_e)):
                print(round(list_e[i], 3), end='      ', file=file)
            print("\n", file=file)

            print("Функция: y =", a, "x +", b, file=file)

            print("Отклонение: S =", s, file=file)

            print("Среднеквадратическое отклонение: sko =", sko, file=file)

            print("Коффициент корреляции Пирсона: r =", final_correlation, file=file)

            print("\n\n")


    return "Линейная", sko, list_f


def secondPolynomialApproximation(list_points, num_print, path):
    num_point = len(list_points)
    list_x = []
    list_y = []
    sum_xy = 0
    sum_x = 0
    sum_x2 = 0
    sum_x3 = 0
    sum_x4 = 0
    sum_y = 0
    sum_x2y = 0
    for i in range(0, num_point, 2):
        sum_xy += list_points[i] * list_points[i + 1]
        list_x.append(list_points[i])
        list_y.append(list_points[i + 1])

        sum_x += list_points[i]
        sum_x2 += list_points[i] ** 2
        sum_x3 += list_points[i] ** 3
        sum_x4 += list_points[i] ** 4

        sum_y += list_points[i + 1]

        sum_x2y += (list_points[i] ** 2) * list_points[i + 1]

    matrix = [[sum_x2, sum_x, num_point / 2, sum_y], [sum_x3, sum_x2, sum_x, sum_xy], [sum_x4, sum_x3, sum_x2, sum_x2y]]

    answer = do_gauss_method(matrix)

    a = answer[0]
    b = answer[1]
    c = answer[2]

    list_f = []
    for i in range(0, len(list_x)):
        list_f.append(a * list_x[i] ** 2 + b * list_x[i] + c)

    list_e = []
    s = 0
    numerator_sko = 0
    for i in range(0, len(list_y)):
        list_e.append(list_f[i] - list_y[i])
        s += list_e[i] ** 2
        numerator_sko += (list_f[i] - list_y[i]) ** 2

    sko = math.sqrt(numerator_sko / len(list_x))

    if num_print == 1:
        print("Полиномиальная функция 2-й степени")

        print("x", end='        ')
        for i in range(0, len(list_x)):
            print(round(list_x[i], 3), end='        ')
        print()

        print("y", end='        ')
        for i in range(0, len(list_y)):
            print(round(list_y[i], 3), end='        ')
        print()

        print("f(x)", end='     ')
        for i in range(0, len(list_f)):
            print(round(list_f[i], 3), end='      ')
        print()

        print("e", end='        ')
        for i in range(0, len(list_e)):
            print(round(list_e[i], 3), end='      ')
        print()

        print("Функция: y =", round(a, 1), "x^2 +", round(b, 1), "x+", round(c, 1))

        print("Отклонение: S =", round(s, 3))

        print("Среднеквадратическое отклонение: sko =", round(sko, 3))
        print("\n\n")

    else:

        with open(path, 'w') as file:
            print("Полиномиальная функция 2-й степени", file=file)

            print("x", end='        ', file=file)
            for i in range(0, len(list_x)):
                print(round(list_x[i], 3), end='        ', file=file)
            print("\n", file=file)

            print("y", end='        ', file=file)
            for i in range(0, len(list_y)):
                print(round(list_y[i], 3), end='        ', file=file)
            print("\n", file=file)

            print("f(x)", end='     ', file=file)
            for i in range(0, len(list_f)):
                print(round(list_f[i], 3), end='      ', file=file)
            print("\n", file=file)

            print("e", end='        ', file=file)
            for i in range(0, len(list_e)):
                print(round(list_e[i], 3), end='      ', file=file)
            print("\n", file=file)

            print("Функция: y =", round(a, 1), "x^2 +", round(b, 1), "x+", round(c, 1), file=file)

            print("Отклонение: S =", round(s, 3), file=file)

            print("Среднеквадратическое отклонение: sko =", round(sko, 3), file=file)
            print("\n\n", file=file)

            print("Data were success write")

    return "Квадратичная", sko, list_f


def thirdPolynomialApproximation(list_points, num_print, path):
    num_point = len(list_points)
    n = num_point / 2
    list_x = []
    list_y = []
    sum_xy = 0
    sum_x = 0
    sum_x2 = 0
    sum_x3 = 0
    sum_x4 = 0
    sum_x5 = 0
    sum_x6 = 0
    sum_y = 0
    sum_x2y = 0
    sum_x3y = 0
    for i in range(0, num_point, 2):
        sum_xy += list_points[i] * list_points[i + 1]
        sum_x2y += (list_points[i] ** 2) * list_points[i + 1]
        sum_x3y += (list_points[i] ** 3) * list_points[i + 1]

        list_x.append(list_points[i])
        list_y.append(list_points[i + 1])

        sum_x += list_points[i]
        sum_x2 += list_points[i] ** 2
        sum_x3 += list_points[i] ** 3
        sum_x4 += list_points[i] ** 4
        sum_x5 += list_points[i] ** 5
        sum_x6 += list_points[i] ** 6

        sum_y += list_points[i + 1]

    matrix = [[sum_x3, sum_x2, sum_x, n, sum_y], [sum_x4, sum_x3, sum_x2, sum_x, sum_xy],
              [sum_x5, sum_x4, sum_x3, sum_x2, sum_x2y], [sum_x6, sum_x5, sum_x4, sum_x3, sum_x3y]]
    answer = do_gauss_method(matrix)

    a = answer[0]
    b = answer[1]
    c = answer[2]
    d = answer[3]

    list_f = []
    for i in range(0, len(list_x)):
        list_f.append(a * list_x[i] ** 3 + b * list_x[i] ** 2 + c * list_x[i] + d)

    list_e = []
    s = 0
    numerator_sko = 0
    for i in range(0, len(list_y)):
        list_e.append(list_f[i] - list_y[i])
        s += list_e[i] ** 2
        numerator_sko += (list_f[i] - list_y[i]) ** 2

    sko = math.sqrt(numerator_sko / len(list_x))

    if num_print == 1:
        print("Полиномиальная функция 3-й степени")

        print("x", end='        ')
        for i in range(0, len(list_x)):
            print(round(list_x[i], 3), end='        ')
        print()

        print("y", end='        ')
        for i in range(0, len(list_y)):
            print(round(list_y[i], 3), end='        ')
        print()

        print("f(x)", end='     ')
        for i in range(0, len(list_f)):
            print(round(list_f[i], 3), end='      ')
        print()

        print("e", end='        ')
        for i in range(0, len(list_e)):
            print(round(list_e[i], 3), end='      ')
        print()

        print("Функция: y =", round(a, 1), "x^3 +", round(b, 1), "x^2 +", round(c, 1), "x + ", round(d, 1))

        print("Отклонение: S =", round(s, 3))

        print("Среднеквадратическое отклонение: sko =", round(sko, 3))
        print("\n\n")

    else:

        with open(path, 'w') as file:
            print("Полиномиальная функция 2-й степени", file=file)

            print("x", end='        ', file=file)
            for i in range(0, len(list_x)):
                print(round(list_x[i], 3), end='        ', file=file)
            print("\n", file=file)

            print("y", end='        ', file=file)
            for i in range(0, len(list_y)):
                print(round(list_y[i], 3), end='        ', file=file)
            print("\n", file=file)

            print("f(x)", end='     ', file=file)
            for i in range(0, len(list_f)):
                print(round(list_f[i], 3), end='      ', file=file)
            print("\n", file=file)

            print("e", end='        ', file=file)
            for i in range(0, len(list_e)):
                print(round(list_e[i], 3), end='      ', file=file)
            print("\n", file=file)

            print("Функция: y =", round(a, 1), "x^3 +", round(b, 1), "x^2 +", round(c, 1), "x + ", round(d, 1),
                  file=file)

            print("Отклонение: S =", round(s, 3), file=file)

            print("Среднеквадратическое отклонение: sko =", round(sko, 3), file=file)
            print("\n\n", file=file)

            print("Data were success write")

    return "Кубическая", sko, list_f


def power_approximation(list_points, num_print, path):
    num_point = len(list_points)
    n = num_point / 2
    list_x = []
    list_y = []

    sum_lnx_lny = 0
    sum_lnx = 0
    sum_lny = 0
    sum_ln2x = 0

    for i in range(0, num_point, 2):
        list_x.append(list_points[i])
        list_y.append(list_points[i + 1])

        sum_lnx_lny += math.log(list_points[i]) * math.log(list_points[i + 1])
        sum_lnx += math.log(list_points[i])
        sum_lny += math.log(list_points[i + 1])
        sum_ln2x += math.log(list_points[i]) ** 2

    b = (n * sum_lnx_lny - sum_lnx * sum_lny) / (n * sum_ln2x - (sum_lnx) ** 2)

    a = math.exp(sum_lny / n - b * sum_lnx / n)

    list_f = []
    for i in range(0, len(list_x)):
        list_f.append(a * list_x[i] ** b)

    list_e = []
    s = 0
    numerator_sko = 0
    for i in range(0, len(list_y)):
        list_e.append(list_f[i] - list_y[i])
        s += list_e[i] ** 2
        numerator_sko += (list_f[i] - list_y[i]) ** 2

    sko = math.sqrt(numerator_sko / len(list_x))

    if num_print == 1:
        print("Степенная функция")

        print("x", end='        ')
        for i in range(0, len(list_x)):
            print(round(list_x[i], 3), end='        ')
        print()

        print("y", end='        ')
        for i in range(0, len(list_y)):
            print(round(list_y[i], 3), end='        ')
        print()

        print("f(x)", end='     ')
        for i in range(0, len(list_f)):
            print(round(list_f[i], 3), end='      ')
        print()

        print("e", end='        ')
        for i in range(0, len(list_e)):
            print(round(list_e[i], 3), end='      ')
        print()

        print("Функция: y =", round(a, 1), "* x ^(", round(b, 1), ")")

        print("Отклонение: S =", round(s, 3))

        print("Среднеквадратическое отклонение: sko =", round(sko, 3))
        print("\n\n")

    else:

        with open(path, 'w') as file:
            print("Степенная функция", file=file)

            print("x", end='        ', file=file)
            for i in range(0, len(list_x)):
                print(round(list_x[i], 3), end='        ', file=file)
            print("\n", file=file)

            print("y", end='        ', file=file)
            for i in range(0, len(list_y)):
                print(round(list_y[i], 3), end='        ', file=file)
            print("\n", file=file)

            print("f(x)", end='     ', file=file)
            for i in range(0, len(list_f)):
                print(round(list_f[i], 3), end='      ', file=file)
            print("\n", file=file)

            print("e", end='        ', file=file)
            for i in range(0, len(list_e)):
                print(round(list_e[i], 3), end='      ', file=file)
            print("\n", file=file)

            print("Функция: y =", round(a, 1), "* x ^(", round(b, 1), ")", file=file)

            print("Отклонение: S =", round(s, 3), file=file)

            print("Среднеквадратическое отклонение: sko =", round(sko, 3), file=file)
            print("\n\n", file=file)

            print("Data were success write")

    return "Степенная", sko, list_f


def exponential_approximation(list_points, num_print, path):
    num_point = len(list_points)
    n = num_point / 2
    list_x = []
    list_y = []

    sum_x2 = 0
    sum_lny = 0
    sum_xlny = 0

    for i in range(0, num_point, 2):
        list_x.append(list_points[i])
        list_y.append(list_points[i + 1])

        sum_x2 += list_points[i] ** 2
        sum_lny += math.log(list_points[i + 1])
        sum_xlny += list_points[i] * math.log(list_points[i + 1])

    b = (n * sum_xlny - sum(list_x) * sum_lny) / (n * sum_x2 - sum(list_x) ** 2)

    a = sum_lny / n - (b * sum(list_x) / n)

    list_f = []
    for i in range(0, len(list_x)):
        list_f.append(math.exp(a + b * list_x[i]))

    list_e = []
    s = 0
    numerator_sko = 0
    for i in range(0, len(list_y)):
        list_e.append(list_f[i] - list_y[i])
        s += list_e[i] ** 2
        numerator_sko += (list_f[i] - list_y[i]) ** 2

    sko = math.sqrt(numerator_sko / len(list_x))

    if num_print == 1:
        print("Экспоненциальная функция")

        print("x", end='        ')
        for i in range(0, len(list_x)):
            print(round(list_x[i], 3), end='        ')
        print()

        print("y", end='        ')
        for i in range(0, len(list_y)):
            print(round(list_y[i], 3), end='        ')
        print()

        print("f(x)", end='     ')
        for i in range(0, len(list_f)):
            print(round(list_f[i], 3), end='      ')
        print()

        print("e", end='        ')
        for i in range(0, len(list_e)):
            print(round(list_e[i], 3), end='      ')
        print()

        print("Функция: y = e^(", round(a, 1), "+", round(b, 1), "* x )")

        print("Отклонение: S =", round(s, 3))

        print("Среднеквадратическое отклонение: sko =", round(sko, 3))
        print("\n\n")

    else:
        with open(path, 'w') as file:
            print("Экспоненциальная функция", file=file)

            print("x", end='        ', file=file)
            for i in range(0, len(list_x)):
                print(round(list_x[i], 3), end='        ', file=file)
            print("\n", file=file)

            print("y", end='        ', file=file)
            for i in range(0, len(list_y)):
                print(round(list_y[i], 3), end='        ', file=file)
            print("\n", file=file)

            print("f(x)", end='     ', file=file)
            for i in range(0, len(list_f)):
                print(round(list_f[i], 3), end='      ', file=file)
            print("\n", file=file)

            print("e", end='        ', file=file)
            for i in range(0, len(list_e)):
                print(round(list_e[i], 3), end='      ', file=file)
            print("\n", file=file)

            print("Функция: y = e^(", round(a, 1), "+", round(b, 1), "* x )", file=file)

            print("Отклонение: S =", round(s, 3), file=file)

            print("Среднеквадратическое отклонение: sko =", round(sko, 3), file=file)
            print("\n\n", file=file)

            print("Data were success write")

    return "Экспоненциальная", sko, list_f


def logarithmic_approximation(list_points, num_print, path):
    num_point = len(list_points)
    n = num_point / 2
    list_x = []
    list_y = []

    sum_ln2x = 0
    sum_ylnx = 0
    sum_lnx = 0

    for i in range(0, num_point, 2):
        list_x.append(list_points[i])
        list_y.append(list_points[i + 1])

        sum_lnx += math.log(list_points[i])
        sum_ln2x += math.log(list_points[i]) ** 2

        sum_ylnx += list_points[i + 1] * math.log(list_points[i])

    b = (n * sum_ylnx - sum(list_y) * sum_lnx) / (n * sum_ln2x - sum_lnx ** 2)

    a = sum(list_y) / n - (b * sum_lnx) / n

    list_f = []
    for i in range(0, len(list_x)):
        list_f.append(a + b * math.log(list_x[i]))

    list_e = []
    s = 0
    numerator_sko = 0
    for i in range(0, len(list_y)):
        list_e.append(list_f[i] - list_y[i])
        s += list_e[i] ** 2
        numerator_sko += (list_f[i] - list_y[i]) ** 2

    sko = math.sqrt(numerator_sko / len(list_x))

    if num_print == 1:
        print("Логарифмическая функция")

        print("x", end='        ')
        for i in range(0, len(list_x)):
            print(round(list_x[i], 3), end='        ')
        print()

        print("y", end='        ')
        for i in range(0, len(list_y)):
            print(round(list_y[i], 3), end='        ')
        print()

        print("f(x)", end='     ')
        for i in range(0, len(list_f)):
            print(round(list_f[i], 3), end='      ')
        print()

        print("e", end='        ')
        for i in range(0, len(list_e)):
            print(round(list_e[i], 3), end='      ')
        print()

        print("Функция: y =", round(a, 1), "+", round(b, 1), "* ln(x)")

        print("Отклонение: S =", round(s, 3))

        print("Среднеквадратическое отклонение: sko =", round(sko, 3))
        print("\n\n")

    else:
        with open(path, 'w') as file:
            print("Логаримическая функция", file=file)

            print("x", end='        ', file=file)
            for i in range(0, len(list_x)):
                print(round(list_x[i], 3), end='        ', file=file)
            print("\n", file=file)

            print("y", end='        ', file=file)
            for i in range(0, len(list_y)):
                print(round(list_y[i], 3), end='        ', file=file)
            print("\n", file=file)

            print("f(x)", end='     ', file=file)
            for i in range(0, len(list_f)):
                print(round(list_f[i], 3), end='      ', file=file)
            print("\n", file=file)

            print("e", end='        ', file=file)
            for i in range(0, len(list_e)):
                print(round(list_e[i], 3), end='      ', file=file)
            print("\n", file=file)

            print("Функция: y =", round(a, 1), "+", round(b, 1), "* ln(x)", file=file)

            print("Отклонение: S =", round(s, 3), file=file)

            print("Среднеквадратическое отклонение: sko =", round(sko, 3), file=file)
            print("\n\n", file=file)

            print("Data were success write")
    return "Логарифмическая", sko, list_f


def best_approximation(sko, name):
    min_sko = min(sko)

    if min_sko == sko[0]:
        return name[0], sko[0]
    elif min_sko == sko[1]:
        return name[1], sko[1]
    elif min_sko == sko[2]:
        return name[2], sko[2]
    elif min_sko == sko[3]:
        return name[3], sko[3]
    elif min_sko == sko[4]:
        return name[4], sko[4]
    else:
        return name[5], sko[5]


def readData(num):
    list_point = []
    if num == 1:
        j = 0
        while j == 0:
            try:
                num_point = int(input("Введите количество точек(значение должно быть от 8 до 12): "))
                if num_point > 12 or num_point < 8:
                    print("Количество точек должно быть от 8 до 12")
                else:
                    j = 1

            except ValueError:
                print("Вы должны ввести число от 8 до 12")

        for i in range(0, num_point):
            j = 0
            while j == 0:
                try:
                    print("Введите x точки ", i + 1)
                    x = int(input())
                    print("Введите y точки ", i + 1)
                    y = int(input())

                    list_point.append(x)
                    list_point.append(y)

                    j = 1
                except ValueError:
                    print("Вы должны ввести число")
        return list_point
    else:
        path = input('\nВведите путь до файла: ').strip()
        while not (os.path.isfile(path) and os.path.getsize(path) > 0):
            print('Файла не существует или он пустой')
            path = input('Повторите ввод: ').strip()

        with open(path, 'r') as file:
            file_line = file.readline()
            file_line = file_line.replace(",", ".")
            num_point = float(file_line)
            for i in range(0, num_point):
                j = 0
                while j == 0:
                    file_line = file.readline()
                    file_line = file_line.replace(",", ".")
                    x = float(file_line)
                    file_line = file.readline()
                    file_line = file_line.replace(",", ".")
                    y = float(file_line)

                    list_point.append(x)
                    list_point.append(y)

                    j = 1

            return list_point


def do_gauss_method(input_matrix):
    check_square_matrix(input_matrix)
    length_of_matrix = len(input_matrix)
    do_triangle_matrix(input_matrix)
    is_singular(input_matrix)
    input_answer_matrix = [0 for i in range(length_of_matrix)]
    for k in range(length_of_matrix - 1, -1, -1):
        input_answer_matrix[k] = (input_matrix[k][-1] - sum(
            [input_matrix[k][j] * input_answer_matrix[j] for j in range(k + 1, length_of_matrix)])) / input_matrix[k][k]

    return input_answer_matrix


def is_singular(input_matrix):
    if count_determinant_for_square_matrix(input_matrix) == 0:
        raise Exception('ERROR: Your matrix is singular (det ~ 0)')


def count_determinant_for_square_matrix(input_matrix):
    determinant = 1
    for i in range(len(input_matrix)):
        determinant *= input_matrix[i][i]
    return round(determinant, 5)


def check_square_matrix(input_matrix):
    for i in range(len(input_matrix)):
        if len(input_matrix) + 1 != len(input_matrix[i]):
            raise Exception('ERROR: The size of matrix isn\'t correct')
        count = 0
        for j in range(len(input_matrix[i]) - 1):
            if input_matrix[i][j] == 0:
                count += 1
        if count == len(input_matrix[i]) - 1:
            raise Exception('ERROR: The matrix has no solutions')


def do_triangle_matrix(input_matrix):
    length_of_matrix = len(input_matrix)
    for k in range(length_of_matrix - 1):
        get_max_element_in_column(input_matrix, k)
        for i in range(k + 1, length_of_matrix):
            div = input_matrix[i][k] / input_matrix[k][k]
            input_matrix[i][-1] -= div * input_matrix[k][-1]
            for j in range(k, length_of_matrix):
                input_matrix[i][j] -= div * input_matrix[k][j]
    return length_of_matrix


def get_max_element_in_column(input_matrix, number_of_column):
    max_element = input_matrix[number_of_column][number_of_column]
    max_row = number_of_column
    for j in range(number_of_column + 1, len(input_matrix)):
        if abs(input_matrix[j][number_of_column]) > abs(max_element):
            max_element = input_matrix[j][number_of_column]
            max_row = j
    if max_row != number_of_column:
        input_matrix[number_of_column], input_matrix[max_row] = input_matrix[max_row], input_matrix[number_of_column]
    return input_matrix


main()

# 0 1
# 2 3
# 4 5
# 6 7
#
#
#
#
