'''Input: n = 4, m = 5
Output: ['*****', '*****', '*****', '*****']'''


def pat(n,m):
    lis = []

    for i in range(n):
        lis.append('*'*m)
    print(lis)


pat(3,2)