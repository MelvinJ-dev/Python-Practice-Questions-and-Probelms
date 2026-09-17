# linear_search([3, 7, 2, 5], 2) should return 2

# linear_search([1, 1, 2, 1], 1) should return 0

# linear_search([], 5) should return -1

# linear_search([4, 2, 8], 6) should return -1

def linear_search(lis,n):

    length = len(lis)-1

    for i in range(length):
        if lis[i]==n:
            return i
    else:
        return -1
pos = linear_search([3,7,2,5],5)
print(pos)