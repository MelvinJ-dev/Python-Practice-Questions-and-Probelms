
# Simple password Cracker
## Works only in a perfect ascending order
# only works for intergers and special characters
import string
import random

def password_cracker_using_for_loop():
    password = [1,2,3,43,75,84,89]

    length = len(password)
    new_lst = []                                                        
    for i in range(length):
        j=0
        for j in range(100):
            if(password[i]==j):
                new_lst.append(j)
    print(new_lst)
# while loop
def password_cracker_using_while_loop():

    sp = [
        "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", 
        "-", "_", "=", "+", "{", "}", "[", "]", ":", ";", 
        "\"", "'", "<", ">", ",", ".", "?", "/", "\\", "|", "~","()"
    ]
    i=0
    s=0
    nw_lst = []
    j=0
    k=0
    passwords = [1,2,3,43,75,84,89,'@',"'",",","()"]
    lenght = len(passwords)
    sp_length = len(sp)

    while True:
        if(type(passwords[i])==int):
            if(len(nw_lst)>=lenght):
                break
            else:
                if(passwords[j]==k):
                    nw_lst.append(k)
                    j+=1
                    i+=1
                else:
                    k+=1                
        else:
            if(len(nw_lst)>=lenght):
                break
            else:
                if(s<=sp_length-1):
                    if(passwords[j]==sp[s]):
                        nw_lst.append(sp[s])
                        j+=1
                    else:
                        s+=1
                else:
                    break
                        
def password_cracker(password):

    characters = [
    # Lowercase letters
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',

    # Uppercase letters
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',

    # Digits
    '0','1','2','3','4','5','6','7','8','9',

    # Special characters
    ' ','`','~','!','@','#','$','%','^','&','*','(',')',
    '-','_','=','+','[',']','{','}','\\','|',';',':',
    "'",'"',',','<','.','>','/','?','()',

    # Extra whitespace
    '\t','\n'
    ]

    print(password)

def password_generator(length):
    letters = string.ascii_letters
    digit = string.digits
    punctuation = string.punctuation
    characters = letters + digit + punctuation
    password=''
    for i in range(length):
        word = random.choice(characters)
        password+=word 
    return password


def password_cracker(password):
    pass


password = password_generator(16)

password_cracker(password)