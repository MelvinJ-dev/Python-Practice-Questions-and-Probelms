# Input: keys = ['a', 'b', 'c'], values = [1, 2, 3]
# Output: {'a': 1, 'b': 2, 'c': 3}

# Input: keys = ['x', 'y', 'z'], values = [10, 20, 30]
# Output: {'x': 10, 'y': 20, 'z': 30}

def merge(lis1,lis2):

    res = {}
    for i in range(len(lis1)):
            if i < len(lis2):
                res[lis1[i]] = lis2[i]
                print(res)
            else:
                print("Out of range")

merge(['a','b','c'],[1,2,3])