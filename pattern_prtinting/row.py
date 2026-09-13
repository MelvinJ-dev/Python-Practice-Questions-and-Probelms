 
def coloum(n):
    lis = []
    for i in range(n):
        row = ''
        for j in range(n):
            row+='*'
        lis.append(row)

    print(lis)

input = int(input("Enter the number : "))

coloum(input)