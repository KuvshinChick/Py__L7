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
    for item in num_list[i_min+1::]:
        abs_sum += abs(item)

    # Замена элементов списка
    for i, item in enumerate(num_list):
        if item < 0:
            num_list[i] = num_list[i]**2

    # Упорядочивание списка
    num_list.sort()
    # Приведение списка к формату двух чисел после запятой
    # num_list = ['%.2f' % elem for elem in num_list]

    print(f"Кол-во отрицательных элементов: {neg_num_sum}")
    print(f"Сумма модулей элементов, расположенных после",  end=' ')
    print(f"минимального по модулю элемента {abs_sum}")
    print(f"Модифицированный массив: {num_list}")



