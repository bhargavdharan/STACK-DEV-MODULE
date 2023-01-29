a = 10

b = 14.5

print(type(a))
print(type(b))

print(isinstance(a,int))

print(isinstance(b,int))


# string 

str1 = 'single quote'
str2 = "double quote"
str3 = '''triple quote'''

# strings are immutable
# str1[0] = "m"

print(str1)
print(str1[0])

print(str2)
print(str3)

# string handling 

# concatenation operation (+)
# str4 = str1 + str2
str4 = str1 + " " + str2
str5 = str1 + " empty space " + str2
print(str4)
print(str5)

# operation(*) for repetation
print(str4*2)

# List
lst1 = ['dharan','ramu','srinu']

print(lst1)

# lists are mutable

lst1[0] = "devi"

print(lst1)

print(lst1[0])

# tuple
tpl1 = ('sri','mike','jay')

print(tpl1)

# tuples are immutable

# tpl1[0] = "rambo"

# print(tpl1)

print(tpl1[0])

# Dictionary

dict1 = {1 : "apple",2 : "orange",3 : "grapes"}

print(dict1)

print(dict1[1])

# print(dict1["apple"])

# set

set1 = {10,20,30,40,50}

print(set1)

print(type(set1))











