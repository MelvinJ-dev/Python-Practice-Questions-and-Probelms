'''Describe how dictionaries are different from lists. When would you use a dictionary over a list?'''

# Phonebook program

print("Example for dictionary")

names = {
    'Melvin' : 4455,
    'Robin'  : 3876,
    'fernando': 8375,
    'prakash' : 3454
}

print(names['Melvin'])

for value,key in names.items():
    print(f"name : {value} , number : {key}")