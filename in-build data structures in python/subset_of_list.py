# Input: lst1 = [1, 2, 3], lst2 = [1, 2, 3, 4, 5]
# Output: True

# All elements in lst1 are present in lst2.

# Input: lst1 = [1, 6], lst2 = [1, 2, 3, 4, 5]
# Output: False

# The element 6 is not present in lst2.

# we have to use bruteforce approach means we need 2 nested loops

# take one element in the 1st list
# compare it with the second list 
# do it for all 
# if any false return false


def check(lis1,lis2):
    
    is_subset = True
    for word in lis1:
        found = False
        for num in lis2:
            if word == num:
                found = True
        if found is False:
            is_subset = False
    print(is_subset)




check([1,6,2,3],[1,2,3,4,5])