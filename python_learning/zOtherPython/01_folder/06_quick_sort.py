from random import shuffle
from time import time

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr.pop(len(arr)//2)
        less = [i for i in arr if i < pivot]
        greater = [i for i in arr if i  > pivot]
    return quicksort(less)+[pivot]+quicksort(greater)

def bubble(array):
    N = len(array)
    for i in range(N-1):
        for j in range(N-i-1):
            if array[j] > array[j+1]:
                buff = array[j]
                array[j] = array[j+1]
                array[j+1] = buff

if __name__ == '__main__':
    arr = list(range(0, 10001))
    shuffle(arr)
    arr1 = list(arr)

    st = time()
    bubble(arr)
    t1 = time() - st

    st = time()
    res = quicksort(arr1)
    t2 = time() - st

    print(t1, t2)
    # print(arr)
    # print(res)
