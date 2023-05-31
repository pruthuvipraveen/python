#while Loops
#How to use while loops to perform repetitive tasks with examples

#Example 1: Counting from 1 to 10

print ("Example 1: Counting from 1 to 10")

i = 1
while i <= 10:
    print (i)
    i = i +1

#Example 2: Reading user input until a specific value is entered

print ("Example 2: Reading user input until a specific value is entered\n")
input_string = ""
while input_string != "quit":
    input_string = input("Enter a word (or 'quit' to exit): ")
    print ("You entered: ",input_string)

    
