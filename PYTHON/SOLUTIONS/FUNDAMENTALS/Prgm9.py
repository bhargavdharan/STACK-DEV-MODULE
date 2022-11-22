# Compount Interest In python

# Formula : A = P(1 + r/n)^n*t
# a - future value of the investment
# P - Prinipal amount
# r - annual rate of interest
# n - number of times that interest is compunded per unit t
# t - time money was invested

# CI = A -P

principal = float(input("Enter the principal amount :"))
rate = float(input("Enter the interest amount :"))
time = float(input("Enter the time in investment :"))
number = float(input("Enter the number of year that interest is compounded per year :"))

# convert rate
rate = rate/100

# calculate total amount
amount = principal * pow(1 + (rate/number),number*time)

# Calculate compound interest
CI = amount - principal

print("Compount Interest : ",CI)
print("Total amount : ",amount)