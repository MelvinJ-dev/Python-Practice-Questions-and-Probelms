'''Input: 3
Output: ['***', '**', '*']'''

def rever(n):
    lis = []
    for i in range(n,0,-1):
        lis.append('*'*i)
    print(lis)

rever(3)