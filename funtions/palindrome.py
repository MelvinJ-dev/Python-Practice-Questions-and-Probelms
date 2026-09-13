## check the word is a palindrome

from colorama import Fore,Style,init

init(autoreset=True)

def checker(word):
    word = word.lower().replace(" ","")
    
    if(word==word[::-1]):
        print(f"the word is {Fore.GREEN}palindrome{Style.RESET_ALL}")
        return True
    else:
        print(f"Not a {Fore.RED}palindrome{Style.RESET_ALL}")
        return False
print("Enter 1 to stop")
while True:
    word = input("Enter the word to check : ")
    if word == '1':
        break
    checker(word)
