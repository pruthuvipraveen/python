#while Loops

print ("Method 1 : \n")

x = 0
while x <5:
    print (x)
    x = x+1
print ("\nMethod 2 : \n")
x = 0
while x <5:
    print (x)
    x +=1

    
#How to avoid infinite loops when using while loops

print ("\nHow to avoid infinite loops when using while loops: \n")

print ("01. Set a maximum number of iterations: \n")

i=0
while i < 10:
    i += 1
    print (i)

print ("\n02. Use a conditional statement: \n")

x = 1
while x != 15:
    print (x)
    x += 1
    

print ("\n03. Avoid using a while loop altogether: \n")

for i in range (21):
    print (i)

print ("\n04. Test your code \n")
print ("05. Use a debugger \n")
    
