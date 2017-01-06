#encoding=utf-8

import random

def rand_diff_int(n, k):
    u"""0~n-1中生成k的不同的随机数."""
    l = [i for i in range(n)]
    result = []
    for j in range(k):
        num = random.randint(j, n-1)
        l[num], l[j] = l[j], l[num]
        result.append(l[j])
    return result


def test_rand_diff_int():
    print rand_diff_int(10, 5)


def binary_search(value, l):
    u"""二分查找."""
    start, end = 0, len(l) - 1
    while start <= end:
        mid = (start + end) / 2
        if value == l[mid]:
            return mid
        elif value > l[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def test_binary_search():
    print binary_search(1, [1, 2, 3, 4, 5])
    print binary_search(5, [1, 2, 3, 4, 5])
    print binary_search(3, [1, 2, 3, 4, 5])
    print binary_search(0, [1, 2, 3, 4, 5])


def get_max_sub_array(l):
    maxsofar, maxending = 0,0
    for i in l:
        maxending = max(maxending + i, 0)
        maxsofar = max(maxsofar, maxending)
    return maxsofar

def test_get_max_sub_array():
    l = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
    print get_max_sub_array(l)

test_get_max_sub_array()
