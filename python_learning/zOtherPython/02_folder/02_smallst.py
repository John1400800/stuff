def find_smallest(lst):
    smallest = lst[0]
    smallest_index = 0
    for index in range(1, len(lst)):
        if lst[index] < smallest:
            smallest = lst[index]
            smallest_index = index
    return smallest_index

print(find_smallest([2, 3 ,5, 6, 7, 0]))
