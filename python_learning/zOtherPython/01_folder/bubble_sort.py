from random import shuffle


def bubblesort(lst):
    lst = list(lst)
    n = len(lst)-1
    for d in range(n):
        for i in range(n-d):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst

if __name__ == '__main__':
    lst = list(range(100))
    shuffle(lst)
    print(bubblesort(lst))
