# Input: 4
# Output: ['   1   ', '  1 2  ', ' 1 2 3 ', '1 2 3 4']
 
# Input: 3
# Output: ['  1  ', ' 1 2 ', '1 2 3']

def num_pyramid(n):
    lis = []
    for i in range(1,n+1):
        num = ''
        for j in range(1,i+1):
            num+=str(j) + " "
        num = num.rstrip()
        fin = num.center(2*n-1)
        lis.append(fin)
    print(lis)

# num_pyramid(4)
num_pyramid(4)

## Learn the single line loop and then begin 