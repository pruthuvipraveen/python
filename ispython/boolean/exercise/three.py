def CheckLeap(year):  
  # Checking if the given year is leap year  
  if((year % 400 == 0) or  
     (year % 100 != 0) and  
     (year % 4 == 0)):   
    print("It's a leap year");  
  # Else it is not a leap year  
  else:  
    print ("It's not a leap year")  

year = int(input("Enter the number: "))  
CheckLeap(year)