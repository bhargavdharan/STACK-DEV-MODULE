# IF statement examples

# Example - 1 : program to check given number is even or not

num = int(input("enter the number :"))

if num%2==0:
    print("Number is even")

# Example - 2 : program to check the largest of all three numbers
    
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

if a>b and a>c:
    print("a is the largest number")

if b>a and b>a:
    print("b is the largest number")

if c>a and c>b:
    print("c is the largest number")
