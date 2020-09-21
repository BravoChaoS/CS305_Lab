from math import log


def find_narcissistic_number(start: int, end: int):
    lst = []

    for i in range(start, end):
        n = int(log(i, 10)) + 1
        s = int(0)
        x = int(i)
        while x > 0:
            s = s + pow(x % 10, n)
            x = x // 10
        # print(s, i)
        if s == i:
            lst.append(i)

    return lst


