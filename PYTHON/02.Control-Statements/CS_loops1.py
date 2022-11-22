# FOR LOOP EXAMPLES

# Example - 1 : Program to show how the for loop works

#-----------Basci level understanding---------------

# creating a for loop
for value in "Python":
    print("Current Letter : ",value)

#---------Intermediate level understanding----------------
# creating a list
fruits = ['apple','banana','orange']

# creating a for loop
for value in fruits:
    print("Current Fruit : ",value)

#---------Complex level understanding-------------------
# creating a list with numbers
numbers = [1,2,3,4,5,6,7,8,9,10]

# variable to store the square of a number
square = 0

# creating an empty list
squares = []

# creating a for loop
for value in numbers:
    square = value**2
    squares.append(square)
    
print("List of squares is ", squares) 

print("=======================================================================")

# Example - 2 : Program to show how if-else statements works with for loop

str = "Python Loop"

# Initializing a loop

for value in str:
    if value == "o":
        print("If Block")
    else:
        print(value)

# For loop with else statement

list = [1,2,3,4,5,6,7,8,9,10]

# Initializing the loop

for value in list:
    if value % 2 != 0:
        print(value)
else:
    print("The above are the only odd numbers available in the given list")

print("=======================================================================")

# Example - 3 : Program to show how range() function works

# range(stop)
# Generate numbers b/w 0 to 6
for value in range(6):
    print(value, end=' ')

print(" ")

# range(start,stop)
# Generate numbers b/w 10 to 20
for value in range(10,20):
    print(value, end=' ')

print(" ")

# range(start,stop,step)
# Generate multiples of 2
for value in range(2,20,2):
    print(value, end=' ')

# iterating a list using for loop

list1 = ['Bahubali','RRR','Bhramastra','Avengers','Avatar','Justice-League']

# iterate a list using range()
for value in range(len(list1)):
    print(list1[value])