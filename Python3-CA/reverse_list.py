def reversed_list(lst1,lst2):
    lst2.reverse()
    return lst1 == lst2
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
