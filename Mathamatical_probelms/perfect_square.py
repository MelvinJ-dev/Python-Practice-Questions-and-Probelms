# Input: num = 16
# Output: True
 
# Input: num = 14
# Output: False
num = 14
def is_perfect_square(num):
    if num <= 0:
        return True
    if num == 1 or num == 2:
        return True
    
    # Only loop up to sqrt(num)
    for i in range(2, num // 2 + 1):  
        if i * i == num:
            return True
        if i * i > num:   # stop early
            break
    return False

status = is_perfect_square(16)
print(status)
