# Input: numbers = [3, 8, 2, 10, 5]
# Output: 10

# Input: numbers = [-5, -10, -2, -1, -7]
# Output: -1


def large_num(numbers):

    large = numbers[0]
    for i in range(len(numbers)):
        if(numbers[i]>large):
            large = numbers[i]
                                        # the logic is wrong            
    print(large)
large_num([33]) 

