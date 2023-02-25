# Implicit Type Convertion - Automatic type convertion

a = 20
b = 23.4

c = a + b

print(c,"\t",type(c))

# Explicit type convertion - Manual type convertion

x = "1"
y = 2

# z = x + y

#print(z,"\t",type(z)) # TypeError: can only concatenate str (not "int") to str
print("before type convertion of x:\t",type(x))
x_ = int(x)
print("After type convertion of x:\t",type(x_))

z = x_ + y
print(z,"\t",type(z))