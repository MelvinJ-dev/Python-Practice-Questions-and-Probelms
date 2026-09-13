# Password strenght checker

'''step1 = get the input
step 2 = check the password length
step 3 = iterate to char one by one and check is there any upper case if yes set flag1 to true
step 4 = second loop inside it where it check for special character if yes set second flag to true 
step 5 = if both the cases satisfied give the password is strong 
step6 = if the 1st case is satisfied say medium add some special character
step 7 = if the 1st case does not satifies say low and add some special character and upper case letter'''



def stre_checker(password):
    length = len(password)
    has_upper = False
    has_specchar = False
    if length<8:
        print ("password should has atleast 8 character")
    else:
        for letter in password:
            if letter.isupper():
                has_upper = True                        # it check only the last character and asign it to flase
            if not letter.isalnum():
                has_specchar = True
        if (has_upper==True and has_specchar== False):
            print("the password do not have a special character")
        elif(has_upper==False and has_specchar==True):
            print("the password do not have a upper case letter ")
        elif(has_upper==False and has_specchar==False):
            print("the password need one upper case and special character")

    if (has_upper==True and has_specchar==True and length>=8):
        print("Password accepted")
        return True
    else:
        print("Password denied..")
        return False

while True:
    password = input("Enter the password : ")
    if stre_checker(password):
        break

    