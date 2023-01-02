# Problem - 9 : program to find leap year or not in python

# user input
year = int(input("Enter a year : "))

# logic to find leap year or not
if (year%400 == 0) and (year%100 == 0):
    print(year," is a leap year")
elif (year%4 == 0) and (year%100 != 0):
    print(year," is a leap year")
else:
    print(year," is not a leap year")

'''
Leap year - A leap year is exactly divisible by 4 except for century years 
(years ending with 00). The century year is a leap year only if it is perfectly divisible by 400. For example,

2017 is not a leap year
2012 is a leap year
'''