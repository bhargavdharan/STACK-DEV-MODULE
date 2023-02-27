
# List of Contents in Python Fundamentals

* MODULES
* COMMENTS
* VARIABLE
* TOKENS & THEIR TYPES
* DATA TYPES

### MODULES

A module is a file containing code written by someone else which can be imported and used in our programs

**PIP**  -  It is the package manager for python. you can use pip to install a module on your system

**Types of Modules**

There are two types of modules in python.

1. Build in modules - pre-installed in python
2. External modules - Need to install using pip

### COMMENTS

Comments are used to write something the programmer does not want to execute

Types of comments

There are two types of comments in python

1. Single-Line Comments  - written using [#comment]()
2. Multi-line Comments - written using [&#34;comment&#34;]()

##### Python Docstring

The strings enclosed in triple quotes that come immediately after the defined function are called Python docstring. It's designed to link documentation developed for Python modules, methods, classes, and functions together. It's placed just beneath the function, module, or class to explain what they perform. The docstring is then readily accessible in Python using the __doc__ attribute.

### VARIABLE

A variable is the name given to a memory location in a program or A variable is container to store values

Example

a = 143 b = "Love" c = 90.3

where a,b,c are the variables that store respective data

The multi-word keywords can be created by the following method.

* **Camel Case -** In the camel case, each word or abbreviation in the middle of begins with a capital letter. There is no intervention of whitespace. For example - nameOfStudent, valueOfVaraible, etc.
* **Pascal Case -** It is the same as the Camel Case, but here the first word is also capital. For example - NameOfStudent, etc.
* **Snake Case -** In the snake case, Words are separated by the underscore. For example - name_of_student, etc.

**Rules of Defining a variable name**

* A variable name contains alphabets, digits, underscores.
* A variable name can only start with alphabet or with an underscore.
* A variable name can't start with a digit
* No whitespaces is allowed to be used-inside a variable name

**Python Variable Types**

There are two types of variables in python - Local and Global Variable.

**Local Variable**

Local variables are the variables that declared inside the function and have scope within the function

```
# Declaring the function
def add():
  # defining local variables - they have a scope withing function
  a = 20
  b = 30
  c = a + b
  print(c)

# calling a function
add()
```

**Code Explanation :** *In the above code, we declared a function named add() and assigned a few variables within the function. These variables will be referred to as the local variables which have scope only inside the function. If we try to use them outside the function, we get a following error*

```
# Declaring the function
def add():
  # defining local variables - they have a scope withing function
  a = 20
  b = 30
  c = a + b
  print(c)

# calling a function
add()

# Accessing local variable outside the function
print(a)
```

We tried to use local variable outside their scope; it threw the **NameError.**

**Global Variable**

Global variables can be used throughout the program, and its scope is in the entire program. We can use global variables inside or outside the function.

A variable declared outside the function is the global variable by default. Python provides the **global** keyword to use global variable inside the function. If we don't use the **global** keyword, the function treats it as a local variable.

```
# Declaring a variable and initialize it
x = 143

# Global variable in function
def mainFn()
  # printing a global variable
  global x
  print(x)
  # Modifying a gloval variable
  x = "Welcome"
  print(x)

mainFn()
print(x)
```

**Code Explanation** :

In the above code, we declare a global variable **x** and assign a value to it. Next, we defined a function and accessed the declared variable using the **global** keyword inside the function. Now we can modify its value. Then, we assigned a new string value to the variable x.

Now, we called the function and proceeded to print  **x** . It printed the as newly assigned value of x.

### TOKENS AND THEIR TYPES

* Tokens can be defined as a punctuator mark, reserved words, and each word in a statement
* Token is the smallest unit inside the given program

#### IDENTIFIERS

An identifier can denote various entities like variable type, subroutines, labels, functions, packges and so on

Example

a = "Deepak Kumar"

where, a is an identifier or a variable

#### LITERALS

Python Literals can be defined as data that is given in a variable or constant.

Python supports the following literals:

1. String Literals
2. Numeric Literals
3. Boolean Literals
4. Special Literals
5. Literal Collections

To know more about literals : [just click here](https://www.javatpoint.com/python-literals)

#### KEYWORD

Python keywords are unique words reserved with defined meanings and functions that we can only apply for those functions. You'll never need to import any keyword into your program because they're permanently present.

Python's built-in methods and classes are not the same as the keywords. Built-in methods and classes are constantly present; however, they are not as limited in their application as keywords.

Assigning a particular meaning to Python keywords means you can't use them for other purposes in our code. You'll get a message of SyntaxError if you attempt to do the same. If you attempt to assign anything to a built-in method or type, you will not receive a SyntaxError message; however, it is still not a smart idea.

Python contains thirty-five keywords in the most recent version, i.e., Python 3.8. Here we have shown a complete list of Python keywords for the reader's reference.

| False  | await    | else    | import   | pass   |
| ------ | -------- | ------- | -------- | ------ |
| None   | break    | except  | in       | raise  |
| True   | class    | finally | is       | return |
| and    | continue | for     | lambda   | try    |
| as     | def      | from    | nonlocal | while  |
| assert | del      | global  | not      | with   |
| async  | elif     | if      | or       | yield  |

In distinct versions of Python, the preceding keywords might be changed. Some extras may be introduced, while others may be deleted. By writing the following statement into the coding window, you can anytime retrieve the collection of keywords in the version you are working on.

Code to check all keywords

`Import keyword #we learn about import fn later

print(keyword.kwlist)`

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

To know more about keyword : [just click here](https://www.javatpoint.com/python-keywords)

#### OPERATORS

The operator can be defined as a symbol which is responsible for a particular operation between two operands. Operators are the pillars of a program on which the logic is built in a specific programming language. Python provides a variety of operators

Example : a + b

a, b are the operands and + is an operator

There are seven operations in python

1. **Arithmetic Operators**  - Arithmetic operators are used to perform arithmetic operations between two operands. It includes + (addition), - (subtraction), *(multiplication), /(divide), %(reminder), //(floor division), and exponent (**) operators.

   * Unary Plus (+)
   * Unary Subtract (-)
   * Multiplication (*)
   * Division (/) - divide left operator withe the right operator and the result is in float
   * Power(**) - Left operator raised to the power of right operand
   * Floor division(//) - division that results in the whole number
   * Modulus (%) - Remainder of the division of left operand by the right

     Note : Floor division can perform both floating and integral aithmetic. if the arguments are in int type then result in int type, if atleast one argument is float type then result is float type
2. **Assignment and Compound Assignment Operators -** The assignment operators are used to assign the value of the right expression to the left operand

   * Compound Assignment Operator

     Combination of Arithmetic and assignment operator is known as compound assignment operator

     Example:

     ```
     x = 5

     '/='

     x /= 5
     print(x)
     ```
3. **Comparison Operators -** Comparison operators are used to comparing the value of the two operands and returns Boolean true or false accordingly.

   * (==) is equal to
   * (>) is greater than
   * (<) is less than
   * (!=) is not equal to
   * (>=) greater than or equal to
   * (<=) less than or equal to
4. **Logical Operators -** The logical operators are used primarily in the expression evaluation to make a decision

   * Logical AND - If both the expression are true, then the condition will be true. If a and b are the two expressions, a → true, b → true => a and b → true.
   * Logical OR - If one of the expressions is true, then the condition will be true. If a and b are the two expressions, a → true, b → false => a or b → true.
   * Logical NOT - 'Not' is used to invert the boolean, and gets the opposite value
5. **Bitwise Operators -** The bitwise operators perform bit by bit operation on the values of the two operands

   ```
   # Detailed Explanation
   if a = 7 and b = 6

   then binary(a) = 0111 and binary(b) = 0110

   Hence a & b = 0011 and a | b = 0111
    a ^ b = 0100 ~ a = 1000
   ```

   * Bitwise AND (&) - If both the bits at the same place in two operands are 1, then 1 is copied to the result. Otherwise, 0 is copied.
   * Bitwise OR (|) - The resulting bit will be 0 if both the bits are zero; otherwise, the resulting bit will be 1.
   * Bitwise XOR (^) - The resulting bit will be 1 if both the bits are different; otherwise, the resulting bit will be 0.
   * Bitwise negation(~) - It calculates the negation of each bit of the operand, i.e., if the bit is 0, the resulting bit will be 1 and vice versa.
   * Bitwsie left shift operator - The left operand value is moved left by the number of bits present in the right operand.
   * Bitwsie right shift operator - The left operand is moved right by the number of bits present in the right operand.
6. **Identity Operators -** The identity operators are used to decide whether an element certain class or type

   * These operators are used to check if two values are located on the same part of the memory
   * Two variables that are equal does not implement that they are identical
     1. 'is' - TRUE if operands are equal
     2. 'is not' - TRUE if operands are not equal
7. **Membership Operators -** Pyton membership operators are used to check the membership of value inside a Python data structure. If the value is present in the data structure, then the resulting value is true otherwise it returns false

   * 'IN' - TRUE if the given object is present in the specified location
   * 'NOT IN' - TRUE if the given object is not present in the specified location

**Operator Precedence**

If multiple operators present then which operator will be evaluated first is decided by operator precedence

The following list describes the operator precendence in the python

Priority order

1. ()
2. **
3. _,~
4. *,/,%,//
5. +,-
6. <<,>>
7. &
8. ^
9. !
10. ==,!=,>,<,>=,<=
11. =,+=,-=,*=
12. is, not is
13. in, not in
14. not
15. and
16. or

### DATA TYPES

Python is the Dynamic typed language that automatically identifies the type of data for us

Python interpreter imlicitly binds the value with its type

`a=5`

The variable **a** holds integer value five and we did not define its type. Python interpreter will automatically interpret variables **a** as an integer type.

Python enables us to check the type of the variable used in the program. Python provides us the **type()** function, which returns the type of the variable passed.

```
a = 5
b = "Hi Python"
c = 25.5
print(type(a))
print(type(b))
print(type(c))
```

Primarily , below are the following data types in python

#### STANDARD DATA TYPES

A variable can hold different types of values. For example, a person's name must be stored as a string whereas its id must be stored as an integer.

Python provides various standard data types that define the storage method on each of them. The data types defined in Python are given below.

1. Numbers (Integer, Complex Number, Float)
2. Sequence Type (Strings, List, Tuple)
3. Boolean
4. Set
5. Dictionary

**NUMBERS TYPE**

Number stores numeric values. The integer, float, and complex values belong to a Python Numbers data-type. Python provides the **type()** function to know the data-type of the variable. Similarly, the **isinstance()** function is used to check an object belongs to a particular class.

```
a = 2
print("The type of a :",type(a))

b = 2.5
print("The type of b :",type(b))

c = 1 + 2j
print("The type of c :",type(c))
print("C is a complex number :",isinstance(1+3j,complex))
```

Python Supports three type of numeric data

1. **Int -** Integer value can be any length such as integers 10, 2, 29, -20, -150 etc. Python has no restriction on the length of an integer. Its value belongs to **int**
2. **Float -** Float is used to store floating-point numbers like 1.9, 9.902, 15.2, etc. It is accurate upto 15 decimal points.
3. **complex -** A complex number contains an ordered pair, i.e., x + iy where x and y denote the real and imaginary parts, respectively. The complex numbers like 2.14j, 2.0 + 2.3j, etc.

**SEQUENCE TYPE**

**String**

The string can be defined as the sequence of characters represented in the quotation marks. In Python, we can use single, double, or triple quotes to define a string.

String handling in Python is a straightforward task since Python provides built-in functions and operators to perform operations in the string.

In the case of string handling, the operator + is used to concatenate two strings as the operation *"hello"+" python"* returns  *"hello python"* .

The operator * is known as a repetition operator as the operation "Python" *2 returns 'Python Python'.

```
# Example of declare a string

str1 = "string using double quotes"
print(str1)

str2 = '''A multiline string'''
print(str2)
```

```
# Example of string handling

str1 = "Hello Madman"
str2 = "How old are you"
print(str1[0:2]) # prints first two character using slice operator
print(str1[4]) # prints 4th character of the string
print(str1*2) # prints the string twice
print(str1 + str2) # prints the concatenation of str1 and str2
```

**List**

Python Lists are similar to arrays in C. However, the list can contain data of different types. The items stored in the list are separated with a comma (,) and enclosed within square brackets [].

We can use slice [:] operators to access the data of the list. The concatenation operator (+) and repetition operator (*) works with the list in the same way as they were working with the strings

```
# Example of list data type

list1 = [1,"Hi","Python",2.5]
list2 = [2,"Hello","Java",3.5]

print(type[list1]) # checks the type of given list

print(list1) # prints the list1

print(list1[3:]) # prints the sliced list of list1

print(list1[0:2]) # prints the sliced list of list1

print(list1 + list2) # prints the concatenated string by using + operator

print(list1*2) # prints the repetation list using * operator

```

**Tuple**

A tuple is similar to the list in many ways. Like lists, tuples also contain the collection of the items of different data types. The items of the tuple are separated with a comma (,) and enclosed in parentheses ().

A tuple is a read-only data structure as we can't modify the size and value of the items of a tuple

```
# Example of tuple

tuple1 = ("hi","Python",5)
tuple2 = ("Hello","Java",10)

print(type(tuple1)) # checks the type of tuple1

print(tuple1) # prints the tuple1

print(tuple1[1:]) # prints the sliced tuple data from tuple1
print(tuple1[0:4]) # prints the sliced tuple data from tuple2

print(tuple1 + tuple2) # prints the concatenated string using + operator

print(tuple1 * 3) # prints the repeated string using * operator

tuple1[2] = "Varun" # If we adds the value to tuple1 - it will throw an error

```

**BOOLEAN**

Boolean type provides two built-in values, True and False. These values are used to determine the given statement true or false. It denotes by the class bool. True can be represented by any non-zero value or 'T' whereas false can be represented by the 0 or 'F'.

```
# Example of Boolean data type

print(type(True))
print(type(False))
print(false)
```

**DICTIONARY**

Dictionary is an unordered set of a key-value pair of items. It is like an associative array or a hash table where each key stores a specific value. Key can hold any primitive data type, whereas value is an arbitrary Python object.

The items in the dictionary are separated with the comma (,) and enclosed in the curly braces {}

```
# Example of dictionary
d = {1:"Dharan",2:"Ram",3:"Srinu",4:"Bhargav"}

print(d) # prints the dictionary

print("First name is ",+d[1]) # we can access values by using keys
print("Second name is ",+d[2])

print(d.keys())
print(d.values())

```

**SET**

Python Set is the unordered collection of the data type. It is iterable, mutable(can modify after creation), and has unique elements. In set, the order of the elements is undefined; it may return the changed sequence of the element. The set is created by using a built-in function **set(),** or a sequence of elements is passed in the curly braces and separated by the comma. It can contain various types of value

```
# Example of set data type

set1 = set()
set2 = {'Dharan',2,5,'Python'}

print(set2) # prints the set values

set2.add("Ramu") # Adding element to the set
print(set2)

set2.remove(2) # Removing element from the set
print(Set2)
```
