# Input: 3
# Output: ['*****', ' *** ', '  *  ', ' *** ', '*****']
 
# Input: 4
# Output: ['*******', ' ***** ', '  ***  ', '   *   ', '  ***  ', ' ***** ', '*******']

def sand_glass(n):

    lis = []
    n = (2*n)-1
    star = "*"
    fin = []
   
    for i in range(n,1,-2):
        lis.append(star*i)

    for j in range(1,n+1,2):
        lis.append(star*j)

    for star in lis:
        centered = star.center(n)
        fin.append(centered)
    print(fin)    
    
sand_glass(3)
