# Input: n = 5
# Output: True
 
# Input: n = 4
# Output: False

def prime(n):
    if n>1:
        for i in range(2,n):
            if n%i == 0:
                print("not a prime")
                break
        else:
            print("prime")
    else:
        print("Not a prime")

prime(2)