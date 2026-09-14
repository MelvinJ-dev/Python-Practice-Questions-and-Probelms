# Input: lst = [1, 7, 3, 10, 5]
# Output: 7

# The maximum difference is between 3 and 10 (i.e., |3 - 10| = 7).

# Input: lst = [10, 11, 15, 3]
# Output: 12

# The maximum difference is between 15 and 3 (i.e., |15 - 3| = 12).

# def find_differece(lis):                                    # O(n) complexity we need O(n^2)

#     greater_digit = 0
#     smaller_digit = 0

#     for i in range(len(lis)-1):
        
#         if (lis[i]<lis[i+1]):
#             if greater_digit < lis[i+1]:
#                 greater_digit = lis[i+1]
#         else:
#             if greater_digit < lis[i]:
#                 greater_digit = lis[i]


#     for i in range(len(lis)-1):
#         if(lis[i]<lis[i+1]):
#             smaller_digit = lis[i]
#         else:
#             smaller_digit = lis[i+1]

#     difference = greater_digit-smaller_digit
#     print(difference)

#     print(greater_digit,smaller_digit)

# Compare every element with every other element.

# Track the largest difference you encounter.

# At the end, you’ll have the difference between the maximum and minimum


# def find_differece(items):
#     diff = [] 
    
#     for i in range(len(items)-1):
#         diffe = items[i]-items[i+1]
#         diff.append(diffe)
#     for i in range(len(diff)-1):
#         larg_diff = diff[0]
#         if diff[i]<diff[i+1]:
#             larg_diff = diff[i+1]

    
#     print(larg_diff)
#     print(diff)

# Input: lst = [1, 7, 3, 10, 5]
# Output: 7

# The maximum difference is between 3 and 10 (i.e., |3 - 10| = 7).

# Input: lst = [10, 11, 15, 3]
# Output: 12

# def find_difference(lis):

#     max_diff = 0
#     diff = []
#     #greater_number,smaller_number = 0

#     for i in range(len(lis)):
#         for j in range(len(lis)):
#             values = abs(lis[i]-lis[j])
            
#             if max_diff < values:
#                 max_diff = values

#                 if(lis[i]<lis[j]):
#                     greater_digit = lis[j]
#                     smaller_digit = lis[i]
#                 else:
#                     greater_digit = len[i]
#                     smaller_digit = len[j]

#     print(max_diff)
#     print(f'greater_digit : {greater_digit}\nsmaller_digit : {smaller_digit}')
#     print(f'difference : {diff}')
# find_difference([1,2,3,4,9])


# def max_consecutive_difference(lst):
#     # Your code goes here
#     max_diff = 0
#     for i in range(len(lst)):
#         for j in range(len(lst)):
            
#             diff = abs(lst[i]-lst[j])
#             if diff > max_diff:
#                 max_diff = diff
#     return max_diff

# num = max_consecutive_difference([1, 7, 3, 10, 5])

# print(num)

# Start with max_diff = 0.
# Use two nested loops:
# Outer loop picks an element at index i.
# Inner loop checks only the next element (j = i+1).
# Compute the absolute difference abs(lst[i] - lst[j]).
# Update max_diff if this difference is larger.
# Continue until all consecutive pairs are tested.

def max_consecutive_difference(lst):
    max_diff = 0
    # Outer loop
    for i in range(len(lst)):
        # Inner loop
        for j in range(len(lst)):
            # Only check consecutive pairs
            if j == i + 1:
                diff = abs(lst[i] - lst[j])
                if diff > max_diff:
                    max_diff = diff
    return max_diff

# Example
num = max_consecutive_difference([1, 7, 3, 10, 5])
print(num)   # Output: 7
