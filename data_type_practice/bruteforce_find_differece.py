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


def find_differece(items):
    diff = [] 
    
    for i in range(len(items)-1):
        diffe = items[i]-items[i+1]
        diff.append(diffe)
    for i in range(len(diff)-1):
        larg_diff = diff[0]
        if diff[i]<diff[i+1]:
            larg_diff = diff[i+1]

    
    print(larg_diff)
    print(diff)
find_differece([20,11,15,3])