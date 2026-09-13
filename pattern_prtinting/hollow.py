def hallow(n):
    lis = []
    for i in range(n):
        if i==0 or i==n-1:
            lis.append('*' * n )
        else:
            lis.append('*' + ' '*(n-2) + '*')
    print(lis)


hallow(5)







