# Input: lst = [1, 2, 3, 4, 5]
# Output: (2, 3)

# There are 2 even numbers: 2, 4

# There are 3 odd numbers: 1, 3, 5

def count_odd_and_even(lis):

    odd_count = 0
    even_count = 0

    for i in range(len(lis)):

        if (lis[i]%2==0):
            even_count+=1
        else:
            odd_count+=1
    return((even_count,odd_count))


num = count_odd_and_even([1,2,3,4,5])
print(num)