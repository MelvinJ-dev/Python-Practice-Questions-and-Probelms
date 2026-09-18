# Input: lst = [12, 11, 13, 5, 6]
# Output: [5, 6, 11, 12, 13]

# Input: lst = [31, 41, 59, 26, 41, 58]
# Output: [26, 31, 41, 41, 58, 59]

def insertion_sort(arr):

    length = len(arr)
    for i in range(length):
        for j in range(length):

            if(arr[i]<arr[j]):
                arr[i],arr[j]=arr[j],arr[i]
    print(arr)   


insertion_sort([31, 41, 59, 26, 41, 58])