# Program to find square of a number

num = 10

square = num * num

print(square)

# Program to convert KM to Miles

# 1 KM = 0.621371 miles
# KM = Miles * 0.621371
# 1 miles = 1.60934 KM 
# Miles = kilometers * 1.60934

# Take input from user
km1 = float(input("Enter your distance in KM :"))

# conversion factor
cFac1 = 1.69034

# calculate miles
mile1 = km1 * cFac1

print("%0.2f kilometers is equal to %0.2f miles"%(km1,mile1))


# Program to convert Miles to KM

# Take input from user
mile2 = float(input("Enter your distance in miles :"))

# conversion factor
cFac2 = 0.621371

# calculate miles
km2 = mile2 * cFac2

print("%0.2f miles is equal to %0.2f Km"%(mile2,km2))
