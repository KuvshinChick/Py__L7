#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Ввести список одной строкой.
    print("Enter ten numbers separated by a space: ")
    num_list = list(map(int, input().split()))
    # Проверить количество элементов списка.
    if len(num_list) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    # Найти искомое произведение.
    # (Условия '>8' '<18' '%10 == 0', дают нам, что элемент равен 10)
    sum_of_nums = 0
    for item in num_list:
        if item == 10:
            sum_of_nums += 1

    print(f"Кол-во элементов: {sum_of_nums}, их произведение: {10**sum_of_nums}")
