# Input: [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]
# Output: {'a': 1, 'b': 5, 'c': 9, 'd': 6}

# Input: [{'x': 10, 'y': 20}, {'y': 30, 'z': 40}, {'z': 50, 'x': 60}]
# Output: {'x': 70, 'y': 50, 'z': 90}

def merger_add(lis):
    new = {}
    for i in lis:
        for key,value in i.items():
            print(key,value)
            new[key] = new.get(key,0)+value
            
    print(new)
            
                


merger_add([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}])