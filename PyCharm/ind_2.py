#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    # Ввести список одной строкой.
    num_list = list(map(float, input().split()))
    # Если список пуст, завершить программу.
    if not num_list:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    # Определить индекс минимального элемента.
    # Найти кол-во отрицательных
    a_min = num_list[0]
    i_min = 0
    neg_num_sum = 0
    for i, item in enumerate(num_list):
        if item < a_min:
            i_min, a_min = i, item
        if item < 0:
            neg_num_sum += 1

    # Нахождение суммы модулей элементов
    abs_sum = 0
    for item in num_list[i_min::]:
        abs_sum += abs(item)

    # Замена элементов списка
    for i in range(len(num_list)):
        num_list[i] = num_list[i] ** 2

    # Упорядочивание списка
    num_list.sort()

    print(f"Кол-во отрицательных элементов: {neg_num_sum}\n"
          f"Сумма модулей элементов, расположенных после "
          f"минимального по модулю элемента {abs_sum}\n"
          f"Модифицированный массив: {num_list}")


