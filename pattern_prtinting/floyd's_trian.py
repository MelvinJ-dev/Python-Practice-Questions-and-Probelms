# Input: 5
# Output: ['1', '2 3', '4 5 6', '7 8 9 10', '11 12 13 14 15']
 
# Input: 3
# Output: ['1', '2 3', '4 5 6']


def fly_tria(n):
    # lis = []
    # num = 0
    # for i in range(1,n+1):
    #     row = ''
    #     for j in range(i):
    #         num+=1
    #         row+=str(num)
    #     lis.append(row)
    # print(lis)

    lis = []
    num = 0
   
    for i in range(1,n+1):
        row = []
        for j in range(i):
            num+=1 
            row.append(str(num))
        row2 = " ".join(row)
        lis.append(row2)
    print(lis)
fly_tria(3)
