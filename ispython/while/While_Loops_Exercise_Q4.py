

num_list = []
num_sum = 0

while True:
    num_input = input ("Please enter a number for done to finish: ")
    if num_input == "done":
        break
    num_list.append(int(num_input))

    index =0
    while index < len (num_list):
        num_sum += num_list [index]
        index +=1

        print ("The sum of the number is :",num_sum)

num_list = []
num_sum = 0

#Read the input from user untill they enter 'done'
while True:
    num_input = input("Please enter a number (or 'done' to finish): ")
    if num_input == 'done':
        break
    num_list.append(int(num_input))

    #Calculate the sum of the numbers using a while loop

    index = 0
    while index < len(num_list):
        num_sum +=num_list[index]
        index +=1

        print("The sum of the numbers is:",+ num sum)
