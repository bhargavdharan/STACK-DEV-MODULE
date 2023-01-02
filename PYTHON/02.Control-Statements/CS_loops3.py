# Example - 3 : Program to print list by using while loop

myList = ["Pepsi","Sprite","7Up","Mountain-Dew","Coke"]

count = 0
while count < len(myList):
    item = myList[count]
    # print(len(item)) - it counts total letters in a item
    print(item) # it displays the item in the list
    count = count + 1
