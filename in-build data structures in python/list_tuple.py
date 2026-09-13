'''Explain the key differences between lists and tuples in Python.
   Provide examples of scenarios where you would choose one over the other.'''


print("Example for list")

# mutable , interate over O(n), preserve index or orderd, 

lis = [1,2,3,4]
print(lis)
lis.append(5)
lis.sort()
print(lis)

print("*****")

print("Example for tuples")

# immutable, check a element is present in O(1), ordered,has other methods to some operations

tup = (1,2,3,4)
print(tup)
print(1 in tup)
print(7 in tup)
