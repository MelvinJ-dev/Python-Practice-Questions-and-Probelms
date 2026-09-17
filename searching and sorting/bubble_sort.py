# # Bubble sort
# Input: lst = [64, 34, 25, 12, 22, 11, 90]
# Output: [11, 12, 22, 25, 34, 64, 90]

# Input: lst = [5, 1, 4, 2, 8]
# Output: [1, 2, 4, 5, 8]

def bubble_sort(lis):
     
    lenght = len(lis)
    for i in range(lenght):
       for j in range(lenght-i-1):
            if(lis[j]>lis[j+1]):
                lis[j],lis[j+1] = lis[j+1],lis[j]
    print(lis)





bubble_sort([64, 34, 25, 12, 22, 90, 11])
