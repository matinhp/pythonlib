from math import *


def make_unique(lst):
    uni_lst = []
    for x in lst:
        if x not in uni_lst:
            uni_lst.append(x)
    return uni_lst


# def sum_function(uni_lst1,uni_lst2):
#     uni_lst = []
#     for x in un:
#         if x not in uni_lst:
#             uni_lst.append(x)
#         return uni_lst


def intersection():
    a = [1, 2, 3, 4, 5, 6]
    b = [5, 6, 7, 8]
    return list(set(a) & set(b))


def is_min(n):
    lst = []
    for i in range(0, n):
        lst.append(int(input('Enter an number:')))
    m = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < m:
            m = lst[i]
    return m


def palindrome(n):
    for i in range(len(n) // 2):
        if n[i] != n[len(n) - i - 1]:
            return False
    else:
        return True


def search(lst, k):
    for i in range(len(lst)):
        if lst[i] == k:
            return i
    return -1
