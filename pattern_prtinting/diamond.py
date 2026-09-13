# Input: 3
# Output: ['  *  ', ' *** ', '*****', ' *** ', '  *  ']
 
# Input: 5
# # Output: ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********',
#                         
#                    ' ******* ', '  *****  ', '   ***   ', '    *    ']


def diamond(n):
    fin = []
    lis2 = []
    lis1 = []
    n = 2*n-1
    space = " "
    star = "*"
    for i in range(1,n+1,2):
        
        strin = ("*"*i).center(n)
        lis1.append(strin)
        
    for j in range(n-2,0,-2):
        
        strin2 = ("*"*j).center(n)
        lis2.append(strin2)


    fin = lis1 + lis2
    print(fin)
    
diamond(3)