def sum_(arr):
    total = 0
    for item in arr:
        total = total + item
    return total

def rec_sum1(arr, sum_=0, index=0):
    if index == len(arr):
        return sum_
    return rec_sum1(arr, sum_+arr[index], index+1)

def rec_sum2(arr):
    if len(arr)==0:
        return 0
    elif len(arr)==1:
        return arr[0]
    return arr[0] + rec_sum2(arr[1:])

lst = [1, 2, 3]
print(rec_sum2(lst))
