'''Describe a real-world scenario where using a tuple would be more appropriate than using a list. 
Explain your reasoning.
INSTRUCTIONS: Consider data integrity and immutability.'''

# In tuples an element is once declared it cannot be modified it will protect the data

tuple1 = (1,2,3,4,5,6,7,8)

print(tuple1)

# tuples can be used in marking the latitute and longitute of the places

location = (1.232,3.4343)

# it can be used in dictioanry as key

locations = {
    (1.232,3.232) : 'Mumbai',
    (2.343,4.545) : 'kolkata',
    (4.343,5.433) : 'chennai'
}

print(locations[(1.232,3.232)])