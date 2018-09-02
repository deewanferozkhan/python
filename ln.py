no1 = float(input("Enter first number- "))
no2 = float(input("Enter second number- "))
no3 = float(input("Enter third number- "))
 
if (no1 > no2) and (no1 > no3):
   largest = no1
elif (no2 > no1) and (no2 > no3):
   largest = no2
else:
   largest = no3
 
print("The largest number is",largest)
