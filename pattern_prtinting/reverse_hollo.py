
# Input: 4
# Output: ['****', '* *', '**', '*']
 
# Input: 5
# Output: ['*****', '*  *', '* *', '**', '*']



def rev_holl_tri(n):

    lis = []
    star = "*"
    space = " "

    for i in range(1,n+1):
        if i==1:
            lis.append(star)
        if i == 2 :
            lis.append(star*i)
        if i>2 and i<n:
            lis.append(star+space+star)
            space+=" "
        if i>1 and i==n:
            lis.append(star*i)
    lis.reverse()  
    print(lis)

rev_holl_tri(5)