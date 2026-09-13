# Input: 4
# Output: ['   *', '  **', ' ***', '****']
 
# Input: 3
# Output: ['  *', ' **', '***']

def rig_tri(n):
    lis = []

    for i in range (1,n+1):
        row = " "
        space = " "
        lis.append(space*(n-i)+"*"*i)
    print(lis)

rig_tri(3)