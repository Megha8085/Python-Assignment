x = 14
y = 10
print(x+y)

n1 = (input("Enter the first number"))
n2 = (input("Enter the second number"))
n3 = (input("Enter the third number"))

if (n1>n2) and (n1>n3):
   largest = n2
elif (n2>n1) and (n2>n3):
   largest = n2
else:
   largest = n3

print("The largest number is",largest)


num = float(input("Input a number:"))
if num >0:
     print("It is a positive number")
elif num == 0:
    print("It is a Zero") 
else:
    print("It is a negative number")