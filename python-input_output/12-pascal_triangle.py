#!/usr/bin/python3
"""trignale pascal func"""


def pascal_triangle(n):
    """return the triangle pascal"""
    if n <= 0:
        return []

    pascal = [[1]]
    while len(pascal) != n:
        pascallen = pascal[-1]
        tmp = [1]
        for i in range(len(pascallen) - 1):
            tmp.append(pascallen[i] + pascallen[i + 1])
        tmp.append(1)
        pascal.append(tmp)
    return pascal
