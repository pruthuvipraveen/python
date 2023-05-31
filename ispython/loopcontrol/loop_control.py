print ("Loop control Statement\n")

print ("1. ‘break’ : The ‘break' statement is used to terminate a loop prematurely")

fruits = ["Apple","Banana","Cherry","Orange","Pear"]
for fruit in fruits:
    if fruit == "Cherry":
        break
    print (fruit)

print ("\n\n2. ‘continue’ : The ‘continue' statement is used to skip the current iteration of a loop and continue with the next iteration")

numbers = [1,2,3,4,5,6,7,8,9,10]

for number in numbers:
    if number % 2 == 0:
        continue
    print (number)


print ("\n\n 3.‘pass’ : The ‘pass' statement is used as a placeholder when a statement is required syntactically, but you don’t want to execute any code")

fruits1 = ["Apple","Banana","Cherry","Orange","Pear"]

for fruit1 in fruits1:
    if fruit1 == "Cherry":
        pass
    else:
        print (fruit1)
    
