# Input: lst = [64, 25, 12, 22, 11]
# Output: [11, 12, 22, 25, 64]

# Input: lst = [29, 10, 14, 37, 13]
# Output: [10, 13, 14, 29, 37]

# [12,25,11,34,90,22]

def selection_sort(lst):
    length = len(lst)
    for i in range(length):
        min_index = i                       # 0
        for j in range(i+1,length):
            if(lst[j]<lst[min_index]):
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    print(lst)
selection_sort([12,25,11,34,90,22])  