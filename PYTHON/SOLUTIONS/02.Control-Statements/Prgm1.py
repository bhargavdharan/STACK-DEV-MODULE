# Problem - 1 : Write a program to develop a simple calculator by using python

# User inputs
num1 = float(input("Enter your first number : "))
num2 = float(input("Enter your second number : "))

print("Welcome to simple calculator")
print("Enter the below operations to perform calculations")
print(" Operations : +, - , * , / ")
select = input("Enter your choosed operation : ")

# check operations and display result

# add(+) two numbers
if select == '+':
    print(num1, " + ", num2, " = " , num1+num2)
# sub(-) two numbers
elif select == "-":
    print(num1, " - ", num2, " = " , num1-num2)
# mul(*) two numbers
elif select == "*":
    print(num1, " * ", num2, " = " , num1*num2)
# div(/) two numbers
elif select == "/":
    print(num1, " / ", num2, " = " , num1/num2)
else:
    print("Invalid output")

