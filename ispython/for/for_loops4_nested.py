# Nested For Loops

print ("How to use nested for loops to loop through multiple lists in Python:\n")

list1 = [1,2,3]
list2 = ["a","b","c"]
list3 = [True,False,True]

for i in list1:
    for j in list2:
        for k in list3:
            print (i,j,k)
