# Swapping of two numbers

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("Values Before Swapping")
print("a = ",a, " and b = ",b)

# Create a temp variable and swap the values
temp = a
a = b
b = temp

# display swapping values
print("Values After Swapping")
print("a = ",a,"and b = ",b)
