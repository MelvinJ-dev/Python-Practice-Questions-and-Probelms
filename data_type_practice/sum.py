# Input: numbers = [1, 2, 3, 4, 5]
# Output: 15

# Input: numbers = [10, -5, 7, 8, -2]
# Output: 18

def sum_of(numbers):
    sum = 0
    for number in numbers:
        sum+=number
    print(sum)

sum_of([1,2,3,4,5]) 
