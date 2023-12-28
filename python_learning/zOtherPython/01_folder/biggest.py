def biggest(arr):
    biggest = arr[0]
    for item in arr[1:]:
        if item>biggest: biggest = item
    return biggest

lst = [10, 3, 4, 6, 4, 8, 7]
print(biggest(lst))
