'''
let take 5
divide 5 by 2 5/2 => 2 - 1
              2/2 => 1 - 0
              1/2 => 0 - 1
'''

num = 5

remind = []

# number = (qoutient*diviser) + reminder

num = 5
remind = []

while num > 0:
    reminder = num % 2        # remainder
    remind.append(reminder)   # collect it
    num = num // 2            # shrink the number

# reverse the list to get proper binary order
remind.reverse()
print(remind)   # [1, 0, 1]
