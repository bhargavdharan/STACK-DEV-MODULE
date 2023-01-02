# Problem - 4 : Program to find the prime factors of an number in python

# Prime factors - Numbers which has only two factors 1 and itself

# 

# User inputs
num = int(input('Enter number : '))

i = 1
# logic to find prime factors
while(i <= num):
    count = 0
    if(num % i == 0):
        j = 1
        while( j <= i):
            if(i % j == 0):
                count = count + 1
            j = j + 1
        if(count == 2):
            print(i, end=" ")
    i = i + 1

print("are the prime factors of number", num)


'''
num = 4

Iteration 1 : value of i = 1
        i <= num --> 1 <= 4 = True
        count = 0
        num % i == 0 --> 4 % 1 == 0 --> True
        j = 1
        j <= i --> i = 1 , j = 1 --> True
        i % j == 0 --> i = 1, j = 1 --> True || count = 1 , j = 2
        count == 2 --> count = 1

Iteration 2 : value of i = 2
        i <= num --> 1 <= 4 = True
        count = 1
        num % i == 0 --> 4 % 2 == 0 --> True
        j = 1
        j <= i --> i = 2 , j = 1 --> True
        i % j == 0 --> i = 2, j = 1 --> True || count = 2 , j = 2
        count == 2 --> count = 2 || print i

Iteration 3 : value of i = 3
        i <= num --> 1 <= 4 = True
        count = 1
        num % i == 0 --> 4 % 3 == 1 --> False    

'''
