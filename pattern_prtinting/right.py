'''Input: 3
Output: ['*', '**', '***']'''


def right(n):
    lis = []

    for i in range(1,n+1):
        lis.append("*"*i)
    print(lis)


right(3)