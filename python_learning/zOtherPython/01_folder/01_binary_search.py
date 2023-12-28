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

def search_rec(lst, item, low=0, high=None):
    if high == None:
        high = len(lst) - 1
    if low > high:
        return None
    mid = (low+high)//2
    if lst[mid] == item:
        return mid
    elif lst[mid] < item:
        return search_rec(lst, item, mid+1, high)
    else:
        return search_rec(lst, item, low, mid-1)

if __name__ == '__main__':
    lst = [ 13, 34, 47, 59 ]
    print(search_rec(lst, 83))
