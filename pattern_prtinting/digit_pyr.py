# Input: 5
# Output: ['1', '22', '333', '4444', '55555']
 
# Input: 3
# Output: ['1', '22', '333']


def dig_pyr(n):
    lis = []

    # for i in range(1,n+1):          # run for n time 5
    #     row = ""
    #     for j in range(1,i+1):         # run for i times 
    #         row+= str(i)
    
    #     lis.append(row)
    # print(lis)
    for i in range(1,n+1):
        lis.append(str(i)*i)
    print(lis)


dig_pyr(5)