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
    # new_list = [y for y in num_list if y > 8 and y < 18 and y % 10 == 0]
    # (Условия '>8' '<18' '%10 == 0', дают нам, что элемент равен 10)
    new_list = [y for y in num_list if y == 10]

    print(f"Кол-во элементов: {len(new_list)}, их произведение: {10 ** len(new_list)}")
