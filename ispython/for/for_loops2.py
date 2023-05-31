#For Loops
#range( ) & enumerate( ) functions

print ("Using ‘range()’ with a For loop\n")

for i in range (5):
    print (i)

print ("\nUsing ‘enumerate()’ with a For loop \n")

fruits = ["Apple", "Banana", "Cherry"]

for i, fruit in enumerate (fruits, start = 1):
    print (i, fruit)

    


