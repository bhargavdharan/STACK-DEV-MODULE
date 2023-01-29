# type conversion

# implicit conversion

# int
a = 10

print(type(a))

# float
b = 20.56

print(type(b))

# float
c = a + b

print(type(c))

# Explicit conversion

str = '23'

# result = a + str

str1 = int(str)

print(type(str1))

result = a + str1

print(result)


print("Good Evening!")
print("it is very peaceful session")

print("Good Evening",end=" ")
print("it is very peaceful session")

print("Hi","How are you ?")
print("Hi","How are you ?",sep=", ")


print("hello","welcome",sep=",",end=" ")
print("to the world!")

x = 10
y = 20

print(x)
print(y)

print("value of x is {} and y is {}".format(x,y))

name = input("enter your name ?")

print("your name is {}".format(name))