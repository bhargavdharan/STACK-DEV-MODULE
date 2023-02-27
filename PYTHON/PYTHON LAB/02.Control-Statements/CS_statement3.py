# ELIF Statement examples

# Example - 1 : Program to check entered number is in the range of 10,50 or 100

num = int(input("Enter your number : "))

if num == 10:
    print("Your number is equal to 10")
elif num == 50:
    print("Your number is equal to 50")
elif num == 100:
    print("Your number is equal to 100")
else:
    print("Entered number is not eaual to 10,50, or 100")

# Example - 2 : Program to check the grade of a student

marks = int(input("Enter the marks : "))

if marks > 85 and marks <= 100:
    print("Congrats! You scored grade A...")
elif marks > 60 and marks <=85:
    print("You scored garde B+...")
elif marks > 40 and marks <=60:
    print("You scored grade B...")
elif marks > 35 and marks <=40:
    print("You scored grade C...")
else:
    print("Sorry! You are failed...!")