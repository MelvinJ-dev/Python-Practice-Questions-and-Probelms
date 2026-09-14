# Input: list1 = [1, 3, 5], list2 = [2, 4, 6]
# Output: [1, 2, 3, 4, 5, 6]

# Input: list1 = [1, 4, 7], list2 = [2, 3, 5, 8]
# Output: [1, 2, 3, 4, 5, 7, 8]

def mer_list(lst1,lst2):

    new_lst = lst1 + lst2
    new_lst.sort()
    print(new_lst)


mer_list([1,3,5],[2,4,6])