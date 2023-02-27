# pyramid number pattern

row = int(input("Enter the number of rows you want : \t"))

for i in range(1,row+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print(" ")

# Output
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6