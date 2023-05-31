#While_Loops_Exercise_Q1
#Write a program that asks the user to enter a number and keeps asking until they enter a number between 1 and 10.

print ("Write a program that asks the user to enter a number and keeps asking until they enter a number between 1 and 10.\n")

num = 0
while num < 1 or num > 10:
    num = int (input ("Please enter a number between 1 and 10: "))

    print ("You entered ", num)
    
    
