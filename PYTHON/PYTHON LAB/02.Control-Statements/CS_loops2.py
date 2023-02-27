# WHILE LOOP EXAMPLES

# Example - 1 : Program to print first 10 natural numbers

num = 10

count = 1

while count <= num:
    print(count, end=" ")
    count = count + 1

print(" ")

# BREAK STATEMENT EXAMPLE
num = 25
count = 1
while count <=num:
    print(count,end=" ")
    count = count + 1
    if count > 5:
        break

print(" ")

# CONTINUE STATEMENT EXAMPLE
num = 15
count = 1

while count <= num:
    if count <= 5:
        count = count + 1
        continue
    print(count,end=" ")
    count = count + 1
    



print(" ")
print("============================================================")

# Example - 2 : Program to print multiples of 2

num2 = 2
count2 = 1

print("The Multiplication table of:",num2)

while count2 <= 12:
    ans = num2 * count2
    print(num2,"X",count2,"=",ans)
    count2 = count2 + 1

print(" ")
print("============================================================")

