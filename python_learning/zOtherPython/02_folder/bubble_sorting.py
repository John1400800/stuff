from random import sample
from datetime import datetime


def bubblesort_once(lst: list):
    len_lst = len(lst)
    cnt = 1
    for _ in range(len_lst - 1):
        for i in range(len_lst - cnt):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        cnt += 1
    return lst


def bubblesort_once2(lst: list):
    len_lst = len(lst)
    for _ in range(len_lst - 1):
        for i in range(len_lst - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst


lst1 = sample(range(1, 10001), 10000)
lst2 = lst1[:]

# start = datetime.now()
# bubblesort_once2(lst1)
# print(datetime.now() - start)

# start = datetime.now()
# bubblesort_once(lst2)
# print(datetime.now() - start)


def bubblesort_once(l: list) -> list:
    res_list = l[:]
    for i in range(len(res_list) - 1):
        if res_list[i] > res_list[i + 1]:
            res_list[i], res_list[i + 1] = res_list[i + 1], res_list[i]

    return res_list


print(bubblesort_once([7, 9, 5, 3, 1, 2, 4, 6, 8]))