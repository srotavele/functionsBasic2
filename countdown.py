from typing import List


def countdown(n):
    list = []
    for i in range(n, 0, -1):
        list.append(i)
    return list


x = countdown(10)


print(x)
