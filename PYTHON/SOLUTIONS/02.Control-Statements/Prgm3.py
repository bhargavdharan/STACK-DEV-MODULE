# Problem - 3 : Program to display a reverse number in python

# User inputs
num = int(input("Enter a number : "))

# logic to find a reverse of a number
reverseN = 0

while(num > 0):
    lastDigit = num % 10
    # print(lastDigit) # for understanding purpose
    reverseN = reverseN * 10 + lastDigit
    # print(reverseN) # for understanding purpose
    num = num // 10
    # print(num) # for understanding purpose


print("The reverse number is = ", reverseN)