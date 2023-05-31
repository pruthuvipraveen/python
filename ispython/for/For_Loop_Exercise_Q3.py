#For_Loop_Exercise_Q3
#Print the sum of all the even numbers from 1 to 50 using a for loop

total = 0
print ("The first 50 even numbers are: \n")
for i in range (2,51,2):
        print (i)
        total = total +i

print ("\nThe sum of the first 50 even numbers are", total)


total = 0
print ("The first 50 odd numbers are: \n")
for i in range (1,51):
    if i % 2 != 0:
        print (i)
        total = total +i

print ("\nThe sum of the first 50 odd numbers are", total)
