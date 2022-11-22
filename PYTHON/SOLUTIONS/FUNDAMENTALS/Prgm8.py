# Simple Interest in Python

# Formula : SI = (PxRxT)/100

P = float(input("Enter the principal amount : "))
R = float(input("Enter the interest amount : "))
T = float(input("Enter the period of time : "))

# Calculate SI
SI = (P*R*T)/100

print("Simple Interest = ",SI)
print("Total amount = ",(P+SI))