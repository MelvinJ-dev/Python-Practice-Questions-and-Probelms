# You are given a list of integers and an integer k. Write a Python function to rotate the list to the ""right" by k positions without using slicing. A rotation shifts elements from the end of the list to the front.

# Parameters:
# lst (List of integers): The list to be rotated.
# k (Integer): The number of positions to rotate the list.
# Returns:
# A list of integers rotated by k positions.
# Example:

# Input: lst = [1, 2, 3, 4, 5], k = 2
# Output: [4, 5, 1, 2, 3]

# Input: lst = [10, 20, 30, 40, 50], k = 3
# Output: [30, 40, 50, 10, 20]

# element = (len(lst)-1)-(k-1)
# new_list = []
# for i in range(element+1):
#     num = lst.pop(element)
#     new_list.append(num)

# print(lst+new_list)

def rot_lis(lst,k):
    if not lst:
        return lst
    k = k%len(lst)
    return lst[-k:] + lst[:-k]

new_list = rot_lis([10,20,30,40,50],3)

print(new_list)