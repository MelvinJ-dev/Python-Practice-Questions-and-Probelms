'''Input: 3
Output: ['  *  ', ' *** ', '*****']             
 
Input: 5
Output: ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********']'''

# def pyramid(n):

#   lis = []
#   space = " "
#   star = "*"
#   no_of_stars = (2*n)-1
#   print(no_of_stars)
#   for j in range(1,no_of_stars+1,2):
#     lis.append(space+star*j+space)
  
#   print(lis)  

# pyramid(3)

def pyramid(n):
    lis = []

    for i in range(1,n+1):
        space = " "*(n-i)
        star = "*"*((2*i)-1)
        lis.append(space+star+space)
    print(lis)


pyramid(5)
# NOT YET COMPLETED 