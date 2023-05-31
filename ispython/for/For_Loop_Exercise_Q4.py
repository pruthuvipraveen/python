#For_Loop_Exercise_Q4
#Given a list of integers, use a for loop to calculate the sum of all the numbers in the list.

total = 0

my_list = [10,20,30,40,50,60,70,80,90,100]
print ("My list of integers are : ")
print (my_list)

for nums in my_list:
    total = total + nums

print ("\nThe sum of this list of integers are : ", total, "\n")
