# How to print number pattern ?

row = 6

# Outer loop
for i in range(row):
    # Inner Loop
    for j in range(i):
        print(i,end=" ")
    # new line after each row
    print('')


# Output
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 