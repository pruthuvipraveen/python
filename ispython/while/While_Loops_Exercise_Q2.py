#While_Loops_Exercise_Q2
# Write a program that asks the user to enter a password and keeps asking until they enter the correct password.


print ("Write a program that asks the user to enter a password and keeps asking until they enter the correct password.")
password = ""
p = input ("Enter you password: ")
while password != p:
    password = input ("Confirm you password: ")
    if (password != p):
            print ("Your password is incorrect!")
    else:
        print ("Your password is correct!")



