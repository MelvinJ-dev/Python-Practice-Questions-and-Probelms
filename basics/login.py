'''Write a Python program that simulates a simple login system. Ask the user for a username and password. 
If the username is "admin" and the password is "password", print "Login successful". Otherwise, print "Login failed".'''



username = input("Enter the username : ")
password = input("Enter the password : ")

if(username=='admin')&(password=='password'):       # it consider it as true or false
    print("Login successful")
else:
    print("Login failed")

