# Input: lst = [1, 2, 3, 4, 5]
# Output: True

# Input: lst = [1, 2, 3, 3, 4, 5]
# Output: False
from colorama import Fore ,Style, init 

init(autoreset=True)

def check_uniq(lis):
    seen = []

    for item in lis:
        if item in seen:
            return False
        seen.append(item)
    return True

status = check_uniq([2,2,3223,3,34])
if status == True:
    print(f'{Fore.GREEN}{status}{Style.RESET_ALL} there is no duplicate')
else:
    print(f'{Fore.RED}{status}{Style.RESET_ALL} there are duplicate in the list')