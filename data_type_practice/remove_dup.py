# Input: lst = [1, 2, 2, 3, 4, 4, 5]
# Output: [1, 2, 3, 4, 5]

# Input: lst = [4, 5, 5, 4, 6, 7]
# Output: [4, 5, 6, 7]

 # get the first integer 
# search the list if it is present again if yes append it to the new list 
# then take second element and search it in the list then append it to te new list

def remove_dupli(numbers):
    result = []
    for number in numbers:             
        if number not in result:
            result.append(number)
    print(result)
remove_dupli([4,5,5,4,6,7])