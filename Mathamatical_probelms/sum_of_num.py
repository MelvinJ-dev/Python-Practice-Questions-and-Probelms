# Input: n = 3
# Output: 12  # (2 + 4 + 6)
 
# Input: n = 5
# Output: 30  # (2 + 4 + 6 + 8 + 10)

def sum_of(n):
    total = 0
    length=2*n+1
    for i in range(2,length,2):
        total+=i
    print(total)

sum_of(5)