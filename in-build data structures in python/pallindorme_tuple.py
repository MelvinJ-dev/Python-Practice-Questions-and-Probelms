# Input: (1, 2, 3, 2, 1)
# Output: True

# Input: ('a', 'b', 'c', 'b', 'a')
# Output: True

# Input: (1, 2, 3, 4, 5)
# Output: False

# Input: ('x', 'y', 'z', 'x')
# Output: False

# Input: ('a',)
# Output: True

def pallindrome(tup1):

    phrase1 = tup1
    phrase2 = tup1[::-1]
    print(phrase2)
    if(phrase1==phrase2):
        print(True)
    else:
        print(False)


pallindrome((1,2,3,2,1))
