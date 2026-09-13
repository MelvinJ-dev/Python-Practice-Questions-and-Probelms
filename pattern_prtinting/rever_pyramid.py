#Input: 3
# Output: ['*****', ' *** ', '  *  ']
 
# Input: 5
# Output: ['*********', ' ******* ', '  *****  ', '   ***   ', '    *    ']


def rev_pyr(n):
    lis = []

    for i in range(1,n+1):
        space = " "*(i-1)
        star = "*"*(2*(n-i)+1)
        lis.append(space+star+space)
    print(lis)
rev_pyr(3)
