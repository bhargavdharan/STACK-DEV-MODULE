# Problem - 2 : Write a program to find fibonnaci series in python
# What is fibonnaci series ?
# The fibonnaci series is a series of numbers where a number is found by adding up the two numbers before it.
# ---starting with 0 and 1, the sequence goes 0,1,1,2,3,5,8,13, and goes on

# User input
num = int(input("Enter number of terms : "))

num1 = 0
num2 = 1

count = 0

# check if the given number is valid or not

if num <= 0:
    print("Dude! Please enter a positive number")

elif num == 1:
    print("The Fibonacci Series : ")
    print(num1)

else:
    print("The Fibonacci Series : ")
    while count < num:
        print(num1, end=" ")
        res = num1 + num2
        num1 = num2
        num2 = res
        count = count + 1
