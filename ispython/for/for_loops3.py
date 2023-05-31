#For Loops

print ("Looping through a string\n")

string = "hello"
for letters in string:
    print (letters)

print ("\nLooping through a list\n")

my_list = [1,2,3,4,5]
for nums in my_list:
    print (nums)

print ("\nLooping through a dictionary\n")

my_dict = {"a":1, "b":2, "c":3}
for keys, values in my_dict.items():
    print (keys,values)

