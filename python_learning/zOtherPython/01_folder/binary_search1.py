def binary_search(lst, item, low=0, high=None):
    if high == None:
        high = len(lst) - 1
    while low <= high:
        mid = (low+high)//2
        guess = lst[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None

lst = [ 13, 34, 47, 59, 64, 71, 83 ]
print(binary_search(lst, 47))
