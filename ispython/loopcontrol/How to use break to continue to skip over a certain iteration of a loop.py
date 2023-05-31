print ("Use ‘continue’ in a ‘for’ loop in Python to skip over even numbers \n")

for i in range (1,11):
    if i % 2 == 0:
        continue
    print (i)

print ("\nUse ‘continue’ in a ‘while’ loop in Python to skip iterations\n")

i = 0
while i< 5:
    i += 1
    if i == 3:
        continue
    print (i)
