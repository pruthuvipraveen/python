print ("Example 1 : use ‘break’ to exit a ‘while’ loop\n")

while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    print ("You entered: ",num)
print ("Loop exited")

print ("\nExample 2 : use ‘break’ to exit a ‘for’ loop\n")

for num in range (1,11):
    if num == 6:
        break
    print (num)

print ("Loop exited")
