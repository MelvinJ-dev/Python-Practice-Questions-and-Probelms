# Input: lst = [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]



def reverse_list(lis):

    rev_lis = []
    last = len(lis)-1

    for i in range(len(lis)):
        rev_lis.append(lis[last])
        last = last - 1
    print(rev_lis)

reverse_list([1,2,3,4,5])