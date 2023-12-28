def find_smallest(lst):
    smallest = lst[0]
    smallest_index = 0
    for index in range(1, len(lst)):
        if lst[index] < smallest:
            smallest = lst[index]
            smallest_index = index
    return smallest_index

def selection_sort(lst):
    lst = list(lst)
    new_lst = []
    for index in range(len(lst)):
        smallest = find_smallest(lst)
        new_lst.append(lst.pop(smallest))
    return new_lst

lst = [3, 1, 4, 2]
print(selection_sort(lst))
