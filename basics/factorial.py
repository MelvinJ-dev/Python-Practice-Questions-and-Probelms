'''
1! = 1 = 1
2! = 1x2 = 2
3! = 1x2x3 = 6
4! = 1x2x3x4 = 24

'''

num = int(input("Enter the number : "))

fact = 1

for i in range(1,num+1):
    fact = fact * i
    print(fact)

print(f"Factorial of the number {num} is {fact}")

   