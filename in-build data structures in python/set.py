'''Write a Python function that takes a list of numbers 
and returns a new list containing only the unique elements, using sets.'''




number = input("Enter the numbers : ")

old_list = []

for i in number.split():
    old_list.append(int(i))
    new_list = old_list

print(f"List : {new_list}")

new_set = set(new_list)

print(f"the duplicate removed set is : {new_set}")



# old_list = []

# number = input("Enter the number : ")

# for i in number.split():
#     old_list.append(int(i))
#     new_list = old_list

# print(f"Final list : {new_list} ")

