# Problem - 8 : Program to print multiplication table

# user input 
num = int(input("Enter a number : "))
count = 1

print("The Multiplication table of:",num)

while count <= 12:
    ans = num * count
    print(num,"X",count,"=",ans)
    count = count + 1