#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sort_func(func):
    def wrapper():
        lst = sorted(func())
        print(f"Отсортированный список: {lst}")

    return wrapper()


@sort_func
def get_list():
    s = input("Строка: ")
    lst = [int(n) for n in s.split(" ")]
    return lst


if __name__ == "__main__":
    get_list()
